from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    # Sanitize input and use full path to executable
    if not host.isalnum() or '..' in host:
        raise ValueError('Invalid host name')
    result = subprocess.run(['/sbin/ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}