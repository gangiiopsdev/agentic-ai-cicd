from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with a list of arguments and shell=False
    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to ensure it is safe
    if not re.match(r'^[a-zA-Z0-9]{1,100}$', host):  # Regex to allow alphanumeric characters and limit length
        raise ValueError("Invalid host input")
    safe_ping(host)
    return {"status": "completed"}