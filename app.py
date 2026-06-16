from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Intentionally hardcoded secrets for research evaluation purposes only
API_KEY = "hardcoded-secret-key-12345"
DB_PASSWORD = "admin123"

@app.route('/')
def home():
    return "Hello from DevSecOps Demo App!"

@app.route('/search')
def search():
    # Intentionally reflects user input for research evaluation purposes
    query = request.args.get('q', '')
    return f"Search results for: {query}"

@app.route('/fetch')
def fetch():
    # Intentionally insecure external request handling for research evaluation purposes
    url = request.args.get('url', '')

    try:
        response = requests.get(url, timeout=5)
        return response.text
    except Exception as e:
        return f"Request failed: {str(e)}"

@app.route('/admin')
def admin():
    # Intentionally exposes hardcoded credentials in response
    # CWE-200: Exposure of Sensitive Information
    return f"Admin panel. Key: {API_KEY}, Password: {DB_PASSWORD}"

if __name__ == '__main__':
    # Debug mode intentionally enabled for research evaluation purposes
    app.run(host='0.0.0.0', port=5000, debug=True)
