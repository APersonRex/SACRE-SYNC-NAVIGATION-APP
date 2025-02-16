from flask import Flask, render_template, jsonify
from flask_cors import CORS  # Fix CORS issues
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return render_template('index.html')  # Main page

@app.route('/new_screen')
def new_screen():
    return render_template('new_screen.html')  # Redirected page

@app.route('/api/locations')
def get_locations():
    geojson_path = os.path.join(os.getcwd(), 'data', 'locations.geojson')  # Ensure correct file path
    try:
        with open(geojson_path) as f:
            locations = json.load(f)
        return jsonify(locations)
    except FileNotFoundError:
        return jsonify({"error": "GeoJSON file not found"}), 404

if __name__ == '__main__':
    ssl_cert = 'cert.pem'
    ssl_key = 'key.pem'

    if not os.path.exists(ssl_cert) or not os.path.exists(ssl_key):
        print("⚠️ SSL certificate or key file not found! Running without HTTPS...")
        app.run(debug=True, host='0.0.0.0', port=5000)  # Run without SSL
    else:
        app.run(debug=True, host='0.0.0.0', port=5000, ssl_context=(ssl_cert, ssl_key))  # Run with HTTPS
