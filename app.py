from flask import Flask, render_template, jsonify, url_for
import os

app = Flask(__name__, static_folder='statics')

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/api/states')
def get_states():
    # This is a placeholder for state data
    # You can replace this with actual data from a database
    states = [
        {"name": "Delhi", "students": 1500, "schools": 45, "lat": 28.7041, "lng": 77.1025},
        {"name": "Maharashtra", "students": 2500, "schools": 78, "lat": 19.0760, "lng": 72.8777},
        {"name": "Karnataka", "students": 1800, "schools": 62, "lat": 12.9716, "lng": 77.5946},
        # Add more states as needed
    ]
    return jsonify(states)

@app.route('/api/statistics')
def get_statistics():
    # This is a placeholder for statistics data
    # You can replace this with actual data from a database
    stats = {
        "total_students": 15000,
        "total_schools": 500,
        "total_states": 15,
        "success_rate": 85
    }
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True)