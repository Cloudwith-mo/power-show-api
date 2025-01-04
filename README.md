# Power API

A simple FastAPI project that provides data about the famous TV show *Power*. The API allows users to retrieve information about the show's cast, seasons, episodes, and more.

## Features

- Retrieve information about the cast of *Power*.
- Access data for all six seasons of the show.
- Get episode titles for specific seasons and episodes.
- Built with FastAPI for fast performance and automatic documentation via Swagger UI.

## API Endpoints

### 1. Get the Cast

**Endpoint**: `/cast`

**Method**: `GET`

**Description**: Retrieve a list of the main cast members from the show *Power*.

### 2. Get Seasons and Episodes

**Endpoint**: `/seasons/{season_number}`

**Method**: `GET`

**Description**: Retrieve a list of episodes for a specific season.

### 3. Get Episode Title

**Endpoint**: `/seasons/{season_number}/episodes/{episode_number}`

**Method**: `GET`

**Description**: Retrieve the title of a specific episode from a specific season.

