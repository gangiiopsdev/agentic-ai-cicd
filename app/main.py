from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_subprocess(command: list):
    for arg in command:
        if '&&' in arg or ';' in arg or '|' in arg or '`' in arg:
            raise ValueError("Unsafe command detected")
    return subprocess.run(command, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_subprocess(["ping", host])

    return {"status": "completed"}