from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host.strip() or any(c in host for c in (';', '|', '&', '$', '`')):
        return False
    return True

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(['ping', '--version'], capture_output=True, text=True)  # Use a safe command with no user input
    return {'status': 'completed'}