from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host parameter to ensure it only contains allowed characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid hostname'}

    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}