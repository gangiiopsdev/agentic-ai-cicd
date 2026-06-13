from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    # Validate host to avoid command injection
    if not host.isalnum() and not any(c in host for c in '-.:/'):
        return 'Invalid host'
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return {'status': safe_ping(host)}