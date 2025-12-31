import json
import pandas as pd

def transform_movies():
    with open('raw_movies.json', 'r') as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    df = df[['title', 'release_date', 'vote_average', 'genre_ids']]  # Select key fields
    df['release_year'] = pd.to_datetime(df['release_date']).dt.year  # Add year
    df['high_rated'] = df['vote_average'] > 7  # Flag
    df['genre_category'] = df['genre_ids'].apply(lambda x: 'Action' if 28 in x else 'Drama')  # Simple categorization (add more)
    df = df[df['high_rated']]  # Filter high-rated
    df.to_csv('transformed_movies.csv', index=False)
    print(f"Transformed {len(df)} high-rated movies to CSV")
    return df

if __name__ == "__main__":
    transform_movies()
