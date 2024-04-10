import streamlit as st 
import pandas as pd
from espn_api.baseball import League

# Call ESPN API
league = League(
    **st.secrets.espn_credentials, # all credentials
#   league_id=st.secrets.espn_credentials.league_id,
#   year=st.secrets.espn_credentials.year,
   debug=True, #debug mode
)

# Get a list of columns for our dataframe
#df_columns = list(league.teams[0].__dict__.keys())

# Remove roster from list of columns
#df_columns.remove('roster')

# Append teams to dataframe
#for d in range(len(league.teams)):
#    team_df = pd.DataFrame(league.teams[d].__dict__, columns=df_columns)
#    league_data = league_data.append(team_df)

# change the index to 'week'
#league_data.index.names = ['week']

# add 'week' column
#league_data.reset_index(level='week', inplace=True)

# add +1 to every week
#league_data['week'] = league_data['week'].apply(lambda x: x + 1)

#st.dataframe(league_data)