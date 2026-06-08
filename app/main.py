from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Sanitize the input to avoid shell injection
    args = ['ping'] + shlex.split(host)
    return args

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = safe_ping(host)
    subprocess.call(safe_host)
    return {"status": "completed"}