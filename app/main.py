from fastapi import FastAPI
import subprocess
import shlex

def ping(host: str):
    # Safe implementation using subprocess.run with proper shell quoting
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with proper shell quoting
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)
    return {"status": "completed"}