from fastapi import FastAPI
import subprocess
def ping(host: str):
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'result': result.stdout if result.returncode == 0 else result.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'result': result.stdout if result.returncode == 0 else result.stderr}