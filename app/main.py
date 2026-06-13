from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/"
)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if re.match(r'^[a-zA-Z0-9.-]+$', host) and '@' not in host:
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}