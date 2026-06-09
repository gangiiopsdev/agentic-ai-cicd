from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host.isdigit():
        return {'error': 'Invalid host provided'}
    args = shlex.split(f"ping {host}")
    result = subprocess.run(args, check=True)
    return {'status': 'completed', 'stdout': result.stdout.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)