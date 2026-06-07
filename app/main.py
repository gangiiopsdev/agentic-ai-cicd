from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or not all(c.isalnum() or c in ['.', '-', '_'] for c in host):  # Allow alphanumeric, '.', '-', and '_' for hostnames
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        subprocess.run(['ping', host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}