from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run instead of shell=True
    subprocess.run(['ping', shlex.quote(host)], check=True)
    return {"status": "completed"}