from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Use shlex.quote to safely handle user input
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout,

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

def ping(host: str):
    status = safe_ping(host)
    return {"status": status}