from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Ensure that only allowed hosts can be pinged
    if host not in ['example.com', 'another.example.com']:
        return {'status': 'error', 'message': 'Invalid host'}

    try:
        # Fixed implementation with exception handling
        subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/safe-ping')
def ping(host: str):
    return safe_ping(host)