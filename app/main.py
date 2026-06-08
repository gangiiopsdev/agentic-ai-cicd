from fastapi import FastAPI
import subprocess
import shlex
guardrails = ['ping', '-c', '1']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Ensure host is safe
    if not all(char.isalnum() or char in ['-'] for char in host):
        return {'status': 'error', 'message': 'Invalid input'}
    # Fixed implementation
    subprocess.call(guardrails + shlex.split(shlex.quote(host)))
    return {'status': 'completed'}