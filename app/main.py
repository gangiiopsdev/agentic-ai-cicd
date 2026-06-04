from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.run with validation
    if not any(char in host for char in [';', '&', '|', '<', '>', '`']):
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid input detected')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Using safe_ping function to avoid command injection
    try:
        safe_ping(host)
    except ValueError as e:
        return {'error': str(e)}
    return {'status': 'completed'}