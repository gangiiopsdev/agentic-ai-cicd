from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.run instead of subprocess.call
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}