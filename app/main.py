from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():  # Basic validation
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)