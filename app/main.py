from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    safe_host = subprocess.quote(host)
    result = subprocess.run(['ping', safe_host], check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        return safe_ping(host)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}