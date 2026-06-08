from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    allowed_hosts = ['example.com', 'another-example.com']
    if host in allowed_hosts:
        args = ['ping', host]
        subprocess.call(args)
    else:
        return {"error": "Invalid host"}

    return {"status": "completed"}