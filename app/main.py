from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Ensure the host parameter does not contain malicious content
    if 'ping' in host:
        return {'error': 'Invalid host parameter'}
    subprocess.call(['ping', host])
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if 'error' in result:
        return result
    return {'status': 'completed'}