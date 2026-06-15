from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using shlex to safely pass arguments
    import shlex
    subprocess.call(['ping'] + shlex.split(host))
    return {"status": "completed"}