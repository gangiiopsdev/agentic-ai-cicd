from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    safe_host = host.strip()  # Remove any leading/trailing whitespace
    if all(c.isalnum() or c in '-.' for c in safe_host):  # Allow alphanumeric characters, hyphens, and dots
        subprocess.call(['ping', safe_host])
    return {'status': 'completed'}