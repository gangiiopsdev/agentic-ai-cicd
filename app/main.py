from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Ensure the host is a valid IP address or hostname to avoid command injection
    if not re.match(r'^[0-9]{1,3}\.[0-9]{1,3}\.?[0-9]{1,3}\.?[0-9]{1,3}$', host):
        raise ValueError('Invalid host format')
    subprocess.run(['ping', host], check=True)

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}