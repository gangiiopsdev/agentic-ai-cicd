from fastapi import FastAPI
import subprocess
import re
def safe_ping(host: str):
    # Validate the host parameter to ensure it contains only allowed characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname or IP address')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Use the safe_ping function to avoid command injection
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}