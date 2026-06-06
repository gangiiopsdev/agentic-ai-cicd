from fastapi import FastAPI
import subprocess
import re

def safe_ping(host: str):
    # Validate host format
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return 'Invalid host'
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e}__FILE__

app = FastAPI()

@app.get('/')
def home():
    return {'"message": "Agentic Self-Healing Pipeline"'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)