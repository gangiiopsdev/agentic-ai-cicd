from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is a valid IP address or hostname
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid input")
    subprocess.call(['ping', host])
    return {"status": "completed"}