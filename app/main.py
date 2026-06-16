from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent command injection
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Implement your validation logic here
    allowed_hosts = ['example.com', '127.0.0.1']  # Example list of allowed hosts
    return host in allowed_hosts