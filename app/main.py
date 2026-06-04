from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using list and check_output with shlex
    if host.isalnum():
        command = ['ping', host]
        subprocess.run(command, shell=False)
    else:
        raise ValueError('Invalid hostname')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}