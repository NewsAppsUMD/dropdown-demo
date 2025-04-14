from flask import Flask, render_template, jsonify
import csv
import os

app = Flask(__name__)

# Load data from CSV file
def load_data():
    data = {}
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, 'md_pres_county.csv')
    
    with open(csv_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            jurisdiction = row['jurisdiction']
            data[jurisdiction] = {
                'harris': int(row['harris']),
                'trump': int(row['trump']),
                'oliver': int(row['oliver']),
                'stein': int(row['stein']),
                'kennedy': int(row['kennedy']),
                'others': int(row['others']),
                'total': int(row['total'])
            }
    return data

# Route for the main page
@app.route('/')
def index():
    data = load_data()
    jurisdictions = list(data.keys())
    return render_template('index.html', jurisdictions=jurisdictions)

# API endpoint to get vote data for a specific jurisdiction
@app.route('/data/<jurisdiction>')
def get_data(jurisdiction):
    data = load_data()
    if jurisdiction in data:
        result = data[jurisdiction]
        # Add percentages to the response
        total = result['total']
        result['percentages'] = {
            'harris': round(result['harris'] / total * 100, 2),
            'trump': round(result['trump'] / total * 100, 2),
            'oliver': round(result['oliver'] / total * 100, 2),
            'stein': round(result['stein'] / total * 100, 2),
            'kennedy': round(result['kennedy'] / total * 100, 2),
            'others': round(result['others'] / total * 100, 2)
        }
        return jsonify(result)
    return jsonify({'error': 'Jurisdiction not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)