from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with shlex.split to prevent shell injection
    import shlex
    subprocess.run(shlex.split(f"ping {host}"), check=True)
    return {"status": "completed"}