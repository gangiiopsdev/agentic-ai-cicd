from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Ensure the host is a valid IP address or hostname before using it in the command
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host provided')
    args = ['ping', host]
    subprocess.call(args)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_safe(host: str):
    ping(host)