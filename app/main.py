from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation with argument validation
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}