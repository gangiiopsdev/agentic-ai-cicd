from fastapi import FastAPI
import os

app = FastAPI()

def safe_ping(host):
    if not host.strip():
        return False
    try:
        # Validate and sanitize the input to prevent command injection
        sanitized_host = host.replace(' ', '')  # Remove spaces from host
        result = subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host format to prevent command injection
    if not host.isalnum() or len(host) > 255:
        return {'error': 'Invalid host'}, 400
    return safe_ping(host)