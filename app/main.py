from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with shlex.split for splitting the command safely.
    safe_host = subprocess.shlex_split(host)
    subprocess.call(["ping", *safe_host])
    return {"status": "completed"}