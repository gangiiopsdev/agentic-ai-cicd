from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate user input to prevent command injection
    if host.strip() != host or any(c in host for c in [';', '&', '|', '`']):
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', host], check=True, text=True)
    return {'status': 'completed'}