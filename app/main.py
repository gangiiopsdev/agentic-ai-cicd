from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate host input to ensure it does not contain malicious characters
    if not is_valid_host(host):
        raise ValueError('Invalid host provided')
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Add logic to validate the host
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return all(char in allowed_chars for char in host)