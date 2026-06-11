from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() or ' ' in host:
        return {'status': 'error', 'error': 'Invalid host name'}
    try:
        output = subprocess.check_output(['ping', quote(host)], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.output.decode()}