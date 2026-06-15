from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    allowed_hosts = ['127.0.0.1', '::1']  # Define a whitelist of allowed hosts
    if host not in allowed_hosts:
        return {'error': 'Invalid host'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}