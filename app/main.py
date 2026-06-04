from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.run without shell=True and validating input
    if not host.replace('.', '', 3).isdigit() or len(host) > 15:
        return {'error': 'Invalid host'}, 400
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}