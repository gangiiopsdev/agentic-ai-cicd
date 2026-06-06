from fastapi import FastAPI
import subprocess
def run_ping(host):
    if not host.isnumeric():
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True, capture_output=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        run_ping(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}