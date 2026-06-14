from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    if host.strip().endswith('.com') or host.strip().endswith('.org'):  # Example validation
        sanitized_host = subprocess.call(['ping', shlex.quote(host)], shell=False)
    else:
        return {'error': 'Invalid host'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_secure(host: str):
    return ping(host)