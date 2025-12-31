# Movie_watchlist_ETL_pipeline
Create a script that pulls movie data (e.g., titles, ratings, genres) from The Movie Database (TMDB) API, cleans/transforms it (e.g., filter high-rated movies, categorize genres), loads to SQLite DB, and queries a simple dashboard-like report.


## Quick Overview
This is a basic ETL script I threw together to practice data engineering. It pulls popular movies from the TMDB API, cleans up the data a bit (like filtering for good ratings and adding a year field), and saves it to a local SQLite database. Then it runs a simple query to show trends, like how many high-rated movies came out each year.

## What It Does
- Grabs movie info (title, rating, genres) from TMDB.
- Filters for movies rated 7+ and tags genres simply (e.g., if it has action ID, call it "Action").
- Loads the cleaned data into a DB table.
- Prints a sample count by release year.

## Setup
1. Clone this repo: `git clone [your-repo-url] && cd movie-etl-pipeline`
2. Install basics: `pip install requests pandas` (sqlite3 comes with Python).
3. Get a free TMDB key from themoviedb.org (just sign up with email).
4. Edit `extract.py` and drop your key in line 3.

## Running It
Fire up the main script: `python etl_pipeline.py`

It'll create:
- `raw_movies.json` (original API dump)
- `transformed_movies.csv` (cleaned version)
- `movie_db.sqlite` (your DB file)

You'll see something like this in the console:
```
   release_year  count
0          2023      8
1          2022      6
...
```

To poke around the DB: `sqlite3 movie_db.sqlite "SELECT * FROM movies LIMIT 5;"`

## Notes
- API has rate limits, so it grabs one page at a time.
- I hardcoded a couple genre checks—easy to add more.
- Learned: Pandas makes transforms a breeze, but watch for null dates.

If you run it and something breaks, check the console errors—probably the API key. Feel free to fork and mess with it.

Cheers :)
