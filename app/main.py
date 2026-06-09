from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Ensure the host is a valid IP or hostname
    if not re.match(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$|^([a-zA-Z0-9]([-a-zA-Z0-9]*[a-zA-Z0-9])?)\.([a-zA-Z0-9]([-a-zA-Z0-9]*[a-zA-Z0-9])?)*$', host):
        raise ValueError('Invalid host format')

    subprocess.call(['ping', shlex.quote(host)])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)