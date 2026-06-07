from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
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
    if host == 'localhost' or host.startswith('127.0.0.1'):
        # Sanitize input to prevent command injection
        safe_host = subprocess.quote(host)
        return safe_ping(safe_host)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}