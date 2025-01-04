# main.py

from fastapi import FastAPI
from data import SHOW_DATA

# Create an app instance
app = FastAPI()

# Welcome endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Power API! Available endpoints: /seasons, /seasons/{season_number}, /seasons/{season_number}/episodes/{episode_number}"}

# Summary endpoint
@app.get("/summary")
def get_summary():
    return {"summary": SHOW_DATA["summary"]}

# Cast endpoint
@app.get("/cast")
def get_cast():
    return {"cast": SHOW_DATA["cast"]}

# Get all seasons and their episode count
@app.get("/seasons")
def get_seasons():
    return {"seasons": SHOW_DATA["seasons"]}

# Get a specific season's details
@app.get("/seasons/{season_number}")
def get_season_details(season_number: int):
    for season in SHOW_DATA["seasons"]:
        if season["season_number"] == season_number:
            return {"season_details": season}
    return {"error": "Season not found"}

# Get all episodes of a specific season
@app.get("/seasons/{season_number}/episodes")
def get_episodes(season_number: int):
    for season in SHOW_DATA["seasons"]:
        if season["season_number"] == season_number:
            return {"episodes": season["episodes"]}
    return {"error": "Season not found"}

# Get the title of a specific episode in a specific season
@app.get("/seasons/{season_number}/episodes/{episode_number}")
def get_episode_title(season_number: int, episode_number: int):
    for season in SHOW_DATA["seasons"]:
        if season["season_number"] == season_number:
            for episode in season["episodes"]:
                if episode["episode_number"] == episode_number:
                    return {"episode_title": episode["title"]}
    return {"error": "Season or episode not found"}