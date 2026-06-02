from fastapi import FastAPI
import subprocess
global_host = '127.0.0.1' # Define a safe default host

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host:
        host = global_host
    # Use subprocess.run with a safe command format to avoid shell injection
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}