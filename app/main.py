from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using shlex.quote
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(f"ping {safe_host}", shell=False)
    return {"status": "completed"}