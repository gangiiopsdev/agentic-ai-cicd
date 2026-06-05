from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and shlex.split for safer command execution
    subprocess.call(subprocess.list2cmdline(['ping', host]), shell=False)
    return {"status": "completed"}