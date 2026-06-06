from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host in ['localhost', '127.0.0.1']:  # Add more allowed hosts as necessary
        subprocess.run(['ping', host], check=True, capture_output=True)
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get(")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    allowed_hosts = ['localhost', '127.0.0.1']  # Add more allowed hosts as necessary
    if host in allowed_hosts:
        subprocess.run(['ping', host], check=True, capture_output=True)
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid host')