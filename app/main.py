from fastapi import FastAPI
import subprocess
cimport re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        raise ValueError("Invalid hostname")
    subprocess.call(f"ping {host}", shell=False)
    return {"status": "completed"}