import streamlit as st 
import pandas as pd
from espn_api.baseball import League

# ESPN League ID
league_id = 6540

# ESPN League Year
year = 2023

# User's ESPN swid
swid = '{0505C567-450F-4315-83D6-528C5D4E3EBB}' 

# USER's espn_s2
espn_s2 = 'AEB2PdDuO%2Bczk7Dcb7nN2zYhyqfOs9H2MlNTpSNkhKVE%2BfdOhugu2ARXYfFxNkyJ5CxIcBzMw7mpUW8D9vZCermbqRrZ7tCd30SKfz%2BMfdIox0V5Sz0w0wQD1GBdb2QJr6OxPTQiTAGm9Djrp4cvxHJZCu2aH7ImasblCNcGzAam2gGk1DxYySc6cXMgdQzC9Ru130p5mvWbK3K7mnroMyJAWAawA9HFn8G2zU3UXUYfJzkYMeg9U5hZ4t3UEeTa2zWpf8HsPqKTWrpbESxGfx1P3mZ1fnoZe2n1C2XulhdHDA%3D%3D' 

# Call ESPN API
league = League(league_id, year, espn_s2, swid)

# Call ESPN API in Debug Mode
# league = League(league_id=1245, year=2018, debug=True)

# Get a list of columns for our dataframe
df_columns = list(league.teams[0].__dict__.keys())

# Remove roster from list of columns
df_columns.remove('roster')

# Append teams to dataframe
for d in range(len(league.teams)):
    team_df = pd.DataFrame(league.teams[d].__dict__, columns=df_columns)
    league_data = league_data.append(team_df)

# change the index to 'week'
league_data.index.names = ['week']

# add 'week' column
league_data.reset_index(level='week', inplace=True)

# add +1 to every week
league_data['week'] = league_data['week'].apply(lambda x: x + 1)

st.dataframe(league_data)