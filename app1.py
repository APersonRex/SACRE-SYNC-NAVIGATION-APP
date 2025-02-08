from flask import Flask, render_template, redirect, url_for , jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Main page with the button

@app.route('/new_screen')  # Change the URL endpoint here
def new_screen():  # Change the function name here
    return render_template('new_screen.html')  # The new page template after redirect

@app.route('/api/locations')
def get_locations():
    with open('data/locations.geojson') as f:
        locations = json.load(f)
    return jsonify(locations)
if __name__ == '__main__':
    # Specify the SSL certificate and key file
    app.run(debug=True, host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem'))  # Enable HTTPS
  