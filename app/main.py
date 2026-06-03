from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safer implementation
    if host.strip() and '.' in host:
        args = ['ping', host]
        subprocess.call(args)
    else:
        raise ValueError('Invalid host parameter')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host.strip() and '.' in host:
        args = ['ping', host]
        subprocess.call(args)
    else:
        raise ValueError('Invalid host parameter')
    return {"status": "completed"}