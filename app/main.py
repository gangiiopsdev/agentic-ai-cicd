from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to avoid command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid host parameter'}

    # Use a safer method to execute the ping command
    try:
        result = subprocess.check_output(['ping', '-c', '4', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': result}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}