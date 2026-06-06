from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safer implementation using subprocess.run with proper sanitization of input
    safe_host = subprocess.quote(host)
    subprocess.run(['ping', safe_host], check=True)
app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping_endpoint(host: str):
    # Safer implementation using subprocess.run with proper sanitization of input
    if not host.isdigit():
        return {'error': 'Invalid input'}, 400
    safe_host = subprocess.quote(host)
    subprocess.run(['ping', safe_host], check=True)
    return {'status': 'completed'}