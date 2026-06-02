from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    sanitized_host = host.strip()
    if not any(char.isalnum() or char in ('.', '-', '_') for char in sanitized_host):
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.call(['ping', sanitized_host])
    return {'status': 'completed'}