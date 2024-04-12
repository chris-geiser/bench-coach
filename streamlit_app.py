import streamlit as st 
import pandas as pd
from espn_api.baseball import League

# Call ESPN API
league = League(
    **st.secrets.espn_credentials, # all credentials
   debug=False, #debug mode
)

team_data = pd.DataFrame.league.teams[0]



# Repeat concatenation into a DataFrame
#lst = []

#for new_row in items_generation_logic:
#    lst.append(new_row)

# create extension
# df_extended = pd.DataFrame(lst, columns=['A', 'B', 'C'])
# or columns=df.columns if identical columns

# concatenate to original
# out = pd.concat([df, df_extended])

# Create Teams DataFrame
# team_data = pd.DataFrame()

# Append teams to DataFrame
# for d in range(len(league.teams)):
#    team_df = league.teams[d].__dict__
#    team_data = team_data.append(team_df, ignore_index=True)

# Create Roster DataFrame
# roster_data = team_data[['team_id','roster']].copy()

# Create Owners DataFrame
# owner_data = team_data[['team_id','owners']].copy()

# Drop unecessary columns
# team_data = team_data.drop(['division_id','division_name','wins','losses','ties','logo_url','final_standing','schedule','owners', 'roster'], axis=1)

#st.dataframe(league_data)
st.header("League Teams")
st.write(team_data)

# st.header("Owner Details")
# st.write(owner_data)

# st.header("Roster Details")
# st.write(roster_data)