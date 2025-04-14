import csv
import os
import sqlite_utils

def load_csv_to_sqlite():
    """
    Load data from the CSV file into a SQLite database using sqlite-utils
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, 'md_pres_county.csv')
    db_path = os.path.join(script_dir, 'election_results.db')
    
    # Create the database if it doesn't exist
    db = sqlite_utils.Database(db_path)
    
    # Check if table already exists and drop it if it does (for fresh reloads)
    if "election_results" in db.table_names():
        db["election_results"].drop()
    
    # Read the CSV file
    records = []
    with open(csv_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            records.append({
                'jurisdiction': row['jurisdiction'],
                'harris': int(row['harris']),
                'trump': int(row['trump']),
                'oliver': int(row['oliver']),
                'stein': int(row['stein']),
                'kennedy': int(row['kennedy']),
                'others': int(row['others']),
                'total': int(row['total'])
            })
    
    # Create the table
    db["election_results"].insert_all(records, pk="jurisdiction")
    
    # Create indexes for faster queries
    db["election_results"].create_index(["jurisdiction"])
    
    print(f"Loaded {len(records)} records into election_results.db")

if __name__ == "__main__":
    load_csv_to_sqlite()