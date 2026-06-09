from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.strip().isdigit() or '@' in host:
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid host input')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)