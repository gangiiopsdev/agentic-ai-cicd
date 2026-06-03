from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote to escape host
    command = ['ping', quote(host)]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        return {'status': 'failed', 'error': result.stderr}
    return {'status': 'completed'}

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping")
def ping_safe(host: str):
    return ping(host)