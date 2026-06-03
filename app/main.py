from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize the input to prevent command injection
    sanitized_host = subprocess.quote(host)
    result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)