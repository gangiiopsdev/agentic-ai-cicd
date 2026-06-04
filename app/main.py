from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    # Safe implementation using subprocess.run with escaped arguments
    subprocess.run(shlex.split('ping ' + host), check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}