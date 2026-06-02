from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def is_valid_host(host):
    # Add your validation logic here
    return host.isdigit()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if is_valid_host(host):  # Validate input
        args = shlex.split('ping ' + host)
        subprocess.run(args, check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}