import streamlit as st 
from espn_api.baseball import League

# League Call
# league = League(league_id: int, year: int, espn_s2: str = None, swid: str = None, debug=False)

# public league
# league = League(league_id=1245, year=2018)

# private league with cookies
league = League(league_id=6540, year=2024, espn_s2='AEB2PdDuO%2Bczk7Dcb7nN2zYhyqfOs9H2MlNTpSNkhKVE%2BfdOhugu2ARXYfFxNkyJ5CxIcBzMw7mpUW8D9vZCermbqRrZ7tCd30SKfz%2BMfdIox0V5Sz0w0wQD1GBdb2QJr6OxPTQiTAGm9Djrp4cvxHJZCu2aH7ImasblCNcGzAam2gGk1DxYySc6cXMgdQzC9Ru130p5mvWbK3K7mnroMyJAWAawA9HFn8G2zU3UXUYfJzkYMeg9U5hZ4t3UEeTa2zWpf8HsPqKTWrpbESxGfx1P3mZ1fnoZe2n1C2XulhdHDA%3D%3D', swid='{0505C567-450F-4315-83D6-528C5D4E3EBB}', debug=True)

# debug mode
# league = League(league_id=1245, year=2018, debug=True)

# won't get any league data when initialized. Make sure to call league.
# fetch_league() when ready to use. 
# league = League(league_id=1245, year=2018, fetch_league=False)



