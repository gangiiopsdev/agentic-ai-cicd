from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with input validation
    if not host.strip():
        raise ValueError('Host parameter cannot be empty or whitespace')
    subprocess.call(['ping', host])
    return {'status': 'completed'}