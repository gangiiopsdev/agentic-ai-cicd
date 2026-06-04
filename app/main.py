from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess_call(command_parts):
    command = ' '.join(shlex.quote(arg) for arg in command_parts)
    return subprocess.call(command, shell=True, executable='/bin/sh')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command_parts = ["ping", host]
    safe_subprocess_call(command_parts)
    return {"status": "completed"}