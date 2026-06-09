from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, check=True)
    return {'status': 'completed'}

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input to ensure it does not contain unexpected characters
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        return {'error': 'Invalid host name'}
    return safe_ping(host)