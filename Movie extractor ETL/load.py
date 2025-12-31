import sqlite3
import pandas as pd

def load_to_db(csv_file='transformed_movies.csv'):
    conn = sqlite3.connect('movie_db.sqlite')
    df = pd.read_csv(csv_file)
    df.to_sql('movies', conn, if_exists='replace', index=False)

    # Sample query: High-rated movies by year
    query = "SELECT release_year, COUNT(*) as count FROM movies GROUP BY release_year ORDER BY count DESC LIMIT 5;"
    result = pd.read_sql_query(query, conn)
    print(result)

    conn.close()
    print("Loaded to movie_db.sqlite + ran sample query")

if __name__ == "__main__":
    load_to_db()