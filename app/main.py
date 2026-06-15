from fastapi import FastAPI
import subprocess
def safe_subprocess(command: list):
    for arg in command:
        if any(dangerous_char in arg for dangerous_char in ['&&', ';', '|', '`']):
            raise ValueError("Unsafe command detected")
    return subprocess.run(command, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_subprocess(["ping", host])
    return {"status": "completed"}