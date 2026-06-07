from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum() or len(host) > 255:
        return {'status': 'error', 'output': 'Invalid input'}
    # Use a whitelist of allowed hosts
    allowed_hosts = ['example.com', 'another.example.com']
    if host not in allowed_hosts:
        return {'status': 'error', 'output': 'Unauthorized host'}
    result = subprocess.run(['ping', '-c', str(4), host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}