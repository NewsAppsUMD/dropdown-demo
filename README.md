# Maryland Presidential Election Results Viewer

This is a simple Flask application that displays the 2024 presidential election results for Maryland counties using a dropdown menu and Chart.js for visualization.

## Features

- Interactive dropdown menu to select different jurisdictions (counties) in Maryland
- Dynamic bar chart visualization of vote totals for each candidate
- Responsive design that works on different screen sizes

## Prerequisites

- Python 3.6 or higher
- Flask
- Peewee
- SQLite Utils

## Setup Instructions

1. Open a new codespace from this repository.

2. Install the required packages:
   ```
   pip install flask sqlite-utils peewee
   ```

3. Setup the database:
   ```
   python init_db.py
   ```

## Running the Application

1. With your virtual environment activated, run the Flask application:
   ```
   python app.py
   ```

   to run the version backed by a database, do this:

   ```
   python app_db.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. Use the dropdown menu to select different jurisdictions and view their respective vote totals.

## Database Structure

The application uses a SQLite database with a single table `election_results` that has the following structure:

- `jurisdiction` (TEXT): Primary key - The name of the county
- `harris` (INTEGER): Vote count for Harris
- `trump` (INTEGER): Vote count for Trump
- `oliver` (INTEGER): Vote count for Oliver
- `stein` (INTEGER): Vote count for Stein
- `kennedy` (INTEGER): Vote count for Kennedy
- `others` (INTEGER): Vote count for other candidates
- `total` (INTEGER): Total votes cast in the jurisdiction

## Customization

- You can modify the chart colors in the `index.html` file
- Add more complex SQL queries in the `app.py` file to extract additional insights
- Extend the database model in `models.py` to add more functionality

## Dependencies

- [Flask](https://flask.palletsprojects.com/): Web framework
- [Peewee](http://docs.peewee-orm.com/): Simple and small ORM
- [sqlite-utils](https://sqlite-utils.datasette.io/): Utility for manipulating SQLite databases
- [Chart.js](https://www.chartjs.org/): JavaScript charting library

## Data Source

The application uses the `md_pres_county.csv` file which contains 2024 presidential election results for Maryland counties.