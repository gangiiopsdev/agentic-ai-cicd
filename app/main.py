from fastapi import FastAPI
import subprocess
g-import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex
    cmd = ['ping', host]
    subprocess.call(cmd)
    return {"status": "completed"}