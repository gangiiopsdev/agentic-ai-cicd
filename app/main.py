from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    # Use a list instead of a string for the command and arguments
    args = ['ping', host]
    subprocess.call(args)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}