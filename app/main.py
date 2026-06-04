from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host.startswith("192.") or host.startswith("172.") or host.startswith("10."):  # Example of basic validation
        subprocess.call(["ping", host])
        return {'status': 'completed'}
    else:
        return {'status': 'invalid host'}, 400