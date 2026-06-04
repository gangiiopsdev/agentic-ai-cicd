from fastapi import FastAPI
import subprocess
def run_safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return run_safe_ping(host)