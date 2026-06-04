from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in host if char in allowed_chars)

def ping(host: str):
    # Sanitize input
    sanitized_host = sanitize_host(host)

    # Validate the URL
    parsed_url = urlparse(sanitized_host)
    if not all([parsed_url.scheme, parsed_url.netloc]):
        return {'status': 'failed', 'error': 'Invalid host format'}

    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

# Example endpoint to test the function
@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)