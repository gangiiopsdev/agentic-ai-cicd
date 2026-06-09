from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f'Ping failed: {result.stderr}')
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if 'localhost' not in host and '127.0.0.1' not in host:
        raise Exception('Invalid host')
    safe_ping(host)
    return {"status": "completed"}