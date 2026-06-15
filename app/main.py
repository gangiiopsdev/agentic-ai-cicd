from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Ensure the host parameter does not contain malicious content
    if 'ping' in host or '&' in host or ';' in host:
        return {'error': 'Invalid host parameter'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if 'error' in result:
        return result
    return result