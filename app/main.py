from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate host input to prevent injection attacks
    if not validate_host(host):
        raise ValueError('Invalid host input')
    subprocess.call(['ping', host])

def validate_host(host: str) -> bool:
    # Simple validation logic (e.g., check for allowed characters)
    return all(c.isalnum() or c in ('.', '-') for c in host)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}