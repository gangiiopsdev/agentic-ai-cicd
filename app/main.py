from fastapi import FastAPI
import subprocess
import re
def validate_host(host):
    return re.match(r'^[a-zA-Z0-9.-]+$', host)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):  # Use a more robust validation function
        return {'status': 'error', 'message': 'Invalid host'}

    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)  # Use check=True to raise an exception on errors
    return {'status': 'completed', 'output': result.stdout}