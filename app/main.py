from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate the host to ensure it's a proper IP address or hostname.
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    subprocess.run(['ping', '-c', '1', host], check=True, shell=False)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}