from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    if not host.strip().isalnum() and not host.strip('0123456789.-').startswith('.'):  # Basic validation for alphanumeric or IP address
        return {'status': 'invalid_host'}
    args = shlex.split(f'ping -c 1 {host}')  # Use specific options to mitigate risks
    subprocess.call(args)
    return {'status': 'completed'}