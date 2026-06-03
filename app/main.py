from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate the host to ensure it's safe to ping
    if not is_safe_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    subprocess.call(shlex.split(' '.join(args)))

# Example of a simple validation function
def is_safe_host(host: str) -> bool:
    return '.' in host and len(host.split('.')) == 4

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}