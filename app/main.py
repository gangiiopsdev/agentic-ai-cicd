from fastapi import FastAPI
import subprocess
import shlex
guardrails = ['ping', '--count=1']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid host'}
    safe_host = shlex.quote(host)
    subprocess.call(guardrails + [safe_host])
    return {'status': 'completed'}