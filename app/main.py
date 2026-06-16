from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    # Add your validation logic here, e.g., whitelist certain domains or IPs
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    args = ['ping'] + shlex.split(host)
    subprocess.run(args, check=True)
    return {'status': 'completed'}