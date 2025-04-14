from load_data import load_csv_to_sqlite
from models import initialize_db

if __name__ == "__main__":
    print("Initializing database...")
    
    # First, create the database tables using Peewee
    initialize_db()
    
    # Then, load the CSV data into the database
    load_csv_to_sqlite()
    
    print("Database initialization complete!")