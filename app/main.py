from fastapi import FastAPI
import subprocess
global ping

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent shell injection
    safe_host = subprocess.list2cmdline([host])
    cmd = ['ping', safe_host]
    subprocess.call(cmd)