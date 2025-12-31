from extract import extract_movies
from transform import transform_movies
from load import load_to_db

if __name__ == "__main__":
    data = extract_movies()
    df = transform_movies()
    load_to_db()
    print("ETL Pipeline Complete!")