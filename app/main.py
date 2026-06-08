from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host parameter to ensure it does not contain malicious input
    allowed_hosts = ['example.com', 'localhost']  # Replace with a whitelist of allowed hosts
    if host in allowed_hosts:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
    else:
        return {'status': 'error', 'message': 'Invalid host'}
    return {'status': 'completed'}

# Fixed code: Use a safe way to execute system commands
@app.get('/safe-ping')
def safe_ping(host: str):
    # Validate the host parameter to ensure it does not contain malicious input
    allowed_hosts = ['example.com', 'localhost']  # Replace with a whitelist of allowed hosts
    if host in allowed_hosts:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid host'}