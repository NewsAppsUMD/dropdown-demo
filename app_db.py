from flask import Flask, render_template, jsonify
from models import ElectionResult, database
import os

app = Flask(__name__)

# Database connection/disconnection handlers
@app.before_request
def before_request():
    database.connect()

@app.after_request
def after_request(response):
    database.close()
    return response

# Route for the main page
@app.route('/')
def index():
    # Get all jurisdictions from the database
    jurisdictions = [result.jurisdiction for result in ElectionResult.select(ElectionResult.jurisdiction).order_by(ElectionResult.jurisdiction)]
    return render_template('index_db.html', jurisdictions=jurisdictions)

# API endpoint to get vote data for a specific jurisdiction
@app.route('/data/<jurisdiction>')
def get_data(jurisdiction):
    try:
        # Query the database for the specified jurisdiction
        result = ElectionResult.get(ElectionResult.jurisdiction == jurisdiction)
        return jsonify(result.to_dict())
    except ElectionResult.DoesNotExist:
        return jsonify({'error': 'Jurisdiction not found'}), 404

# API endpoint to get statewide totals
@app.route('/data/statewide')
def get_statewide():
    # Calculate statewide totals using SQL aggregation
    query = ElectionResult.select(
        fn.SUM(ElectionResult.harris).alias('harris'),
        fn.SUM(ElectionResult.trump).alias('trump'),
        fn.SUM(ElectionResult.oliver).alias('oliver'),
        fn.SUM(ElectionResult.stein).alias('stein'),
        fn.SUM(ElectionResult.kennedy).alias('kennedy'),
        fn.SUM(ElectionResult.others).alias('others'),
        fn.SUM(ElectionResult.total).alias('total')
    )
    
    results = query.dicts().get()
    
    # Calculate percentages
    total = results['total']
    results['percentages'] = {
        'harris': round(results['harris'] / total * 100, 2),
        'trump': round(results['trump'] / total * 100, 2),
        'oliver': round(results['oliver'] / total * 100, 2),
        'stein': round(results['stein'] / total * 100, 2),
        'kennedy': round(results['kennedy'] / total * 100, 2),
        'others': round(results['others'] / total * 100, 2)
    }
    
    results['jurisdiction'] = 'Statewide'
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)