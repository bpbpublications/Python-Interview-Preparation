from flask import Flask, request, redirect, jsonify
import base64
import hashlib
import random
 
app = Flask(__name__)
 
# In-memory storage (for simplicity)
url_map = {}  # short_url: long_url
base_url = "<https://short.ly/>"
 
# Function to generate a short URL
def generate_short_url(long_url):
    # Use a hashing algorithm (e.g., MD5) and Base64 encode it
    hash_object = hashlib.md5(long_url.encode())
    short_url = base64.urlsafe_b64encode(hash_object.digest()[:6]).decode('utf-8')
    return short_url
 
# API to shorten the URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.json['long_url']
 
    # Check if the URL is already shortened
    for short, long in url_map.items():
        if long == long_url:
            return jsonify({'short_url': base_url + short})
 
    # Generate a short URL
    short_url = generate_short_url(long_url)
 
    # Store the mapping
    url_map[short_url] = long_url
 
    return jsonify({'short_url': base_url + short_url})
 
# API to redirect to the original URL
@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = url_map.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return jsonify({'error': 'Short URL not found'}), 404
 
if __name__ == "__main__":
    app.run(debug=True)
