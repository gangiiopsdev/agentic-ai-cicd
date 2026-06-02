from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host to ensure it's a safe target for pinging
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}

    # Secure implementation using a list of arguments to avoid shell injection
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}