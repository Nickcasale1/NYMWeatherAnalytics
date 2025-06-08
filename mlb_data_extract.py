import requests
import pandas as pd
import sqlite3
from datetime import datetime, timedelta

today = datetime.today()

# Calculate yesterday's date by subtracting one day
yesterday = today - timedelta(days=1)

# Extract only the date part
yesterday_date = yesterday.date()

team = 'NYM'

def get_mlb_game_data(team, yesterday_date):
    url = f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={yesterday_date}"
    res = requests.get(url)
    data = res.json()
    dataDF = pd.DataFrame(data)
    games = pd.json_normalize(dataDF['dates'][0]['games'])
    mets_games = games[
    (games['teams.home.team.name'] == 'New York Mets') |
    (games['teams.away.team.name'] == 'New York Mets')
]

    return mets_games


game_data = get_mlb_game_data(team, yesterday_date)
print(game_data)