from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input
    if not host.isalnum() or '-' not in host:
        raise ValueError('Invalid host input')
    # Use full executable path to mitigate the risk of shell injection
    subprocess.run(['/bin/ping', host], check=True)
    return {'status': 'completed'}