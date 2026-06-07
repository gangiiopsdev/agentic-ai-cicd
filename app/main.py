from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Secure implementation
    cmd = ["ping", *shlex.split(host)]
    subprocess.call(cmd)
    return {"status": "completed"}