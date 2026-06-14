from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to avoid shell injection
    if re.match(r'^[a-zA-Z0-9.-]+$', host):
        args = ['ping', host]
        subprocess.run(args, check=True)
        return {"status": "completed"}
    else:
        raise ValueError("Invalid host name")