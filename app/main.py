from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent code injection
    args = ['ping'] + shlex.split(host.replace(';', ''))
    subprocess.call(args)
    return {"status": "completed"}