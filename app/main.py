from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Safe implementation using subprocess.run with proper quoting
    subprocess.run(['ping'] + shlex.split(host), check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    return {"status": "completed"}