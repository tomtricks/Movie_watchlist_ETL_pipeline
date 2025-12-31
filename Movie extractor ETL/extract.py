import requests
import json

API_KEY = 'your_tmdb_key_here'  # Replace with yours
BASE_URL = 'https://api.themoviedb.org/3'

def extract_movies(num_movies=100):
    url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&page=1"
    response = requests.get(url)
    data = response.json()['results'][:num_movies]
    with open('raw_movies.json', 'w') as f:
        json.dump(data, f)
    print(f"Extracted {len(data)} movies to raw_movies.json")
    return data

if __name__ == "__main__":
    extract_movies()