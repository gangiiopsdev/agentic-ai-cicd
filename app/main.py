from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize the host input
    if not all(c.isalnum() or c in ['-', '.'] for c in host):
        raise ValueError('Invalid host name')
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    args = ['ping', safe_ping(host)]
    subprocess.call(args)
    return {"status": "completed"}