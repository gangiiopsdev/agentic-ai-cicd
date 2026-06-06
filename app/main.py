from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    if not host.isnumeric():
        raise ValueError("Invalid host")
    subprocess.call(['ping', host], shell=False)

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