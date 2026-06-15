from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess with args instead of shell=True
    if host == 'localhost' or host in ['127.0.0.1', '::1']:  # Improved validation
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'result': result.stdout}
    else:
        return {'status': 'failed', 'reason': 'Invalid host'}