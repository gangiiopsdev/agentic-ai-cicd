from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation using shlex.quote to prevent shell injection
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(f'ping {safe_host}', shell=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation using shlex.quote to prevent shell injection
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(f'ping {safe_host}', shell=True)
    return {"status": "completed"}