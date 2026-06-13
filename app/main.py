from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    try:
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}
    return {'status': 'completed'}
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_route(host: str):
    # Validate input to prevent injection attacks
    if not host.strip().isalnum() or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)