from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum():
        return {'error': 'Invalid hostname'}
    result = subprocess.run(['ping', '--'], [host], capture_output=True, text=True)
    return {'status': result.stdout}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)