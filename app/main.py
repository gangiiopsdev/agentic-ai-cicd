from fastapi import FastAPI
import subprocess
def run_ping(host):
    return subprocess.call(['ping', '-c', '1', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in ['-', '_'] for c in host):
        return {'error': 'Invalid input'}, 400
    return run_ping(host)