from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host or ' ' in host:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        # Use a whitelist of allowed hosts
        allowed_hosts = ['127.0.0.1', '::1']  # Add more allowed hosts as needed
        if host not in allowed_hosts:
            return {'status': 'failed', 'error': 'Invalid host'}
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}