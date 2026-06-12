from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    cmd = ["ping", host]
    subprocess.call(cmd, shell=False)
    return {"status": "completed"}