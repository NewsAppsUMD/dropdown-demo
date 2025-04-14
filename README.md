# Maryland Presidential Election Results Viewer

This is a simple Flask application that displays the 2024 presidential election results for Maryland counties using a dropdown menu and Chart.js for visualization.

## Features

- Interactive dropdown menu to select different jurisdictions (counties) in Maryland
- Dynamic bar chart visualization of vote totals for each candidate
- Responsive design that works on different screen sizes

## Prerequisites

- Python 3.6 or higher
- Flask

## Setup Instructions

1. First, clone or download this repository to your local machine.

2. Create a virtual environment (recommended):
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install flask
   ```

5. Make sure your project structure looks like this:
   ```
   project-folder/
   ├── app.py
   ├── md_pres_county.csv
   ├── templates/
   │   └── index.html
   └── README.md
   ```

6. Create the `templates` directory if it doesn't exist:
   ```
   mkdir templates
   ```

7. Move the `index.html` file into the `templates` directory.

## Running the Application

1. With your virtual environment activated, run the Flask application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. Use the dropdown menu to select different jurisdictions and view their respective vote totals.

## Customization

- You can modify the chart colors in the `index.html` file
- Additional data or features can be added by extending the Flask routes in `app.py`

## Dependencies

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Chart.js](https://www.chartjs.org/) - JavaScript charting library

## Data Source

The application uses the `md_pres_county.csv` file which contains 2024 presidential election results for Maryland counties.
