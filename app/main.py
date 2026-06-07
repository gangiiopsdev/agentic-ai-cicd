from fastapi import FastAPI
import subprocess

def generate_ping_command(host: str):
    return ['ping', host]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum() or len(host) > 64:
        return {'status': 'error', 'message': 'Invalid host provided'}
    subprocess.call(generate_ping_command(host))
    return {'status': 'completed'}