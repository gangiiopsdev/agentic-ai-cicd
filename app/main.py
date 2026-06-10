from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Safe implementation using a list for subprocess arguments and validating input
    if not host.isdigit():
        raise ValueError('Invalid host')
    args = ['ping', host]
    subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}