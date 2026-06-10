from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Secure implementation using subprocess.run with validation
    if not host.replace('.', '').isalnum():
        raise ValueError('Invalid host name')
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return ping(host)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}