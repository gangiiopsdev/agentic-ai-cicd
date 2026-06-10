from fastapi import FastAPI
import subprocess

def run_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'
global_config = {'allow_subprocess': False}

if global_config['allow_subprocess']:
    app = FastAPI()
else:
    raise Exception('Subprocess execution is disabled')

@app.get(")
def home():
    return {
        "message": "Agentic Self-Healing Pipeline"
    }

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum():
        raise ValueError('Invalid input')
    # Use a whitelist of allowed hosts
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Host not allowed')
    return run_ping(host)