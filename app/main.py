from fastapi import FastAPI
import subprocess
c import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not all(c in string.ascii_letters or c.isdigit() for c in host):
        raise ValueError("Invalid hostname")
    try:
        output = subprocess.run(["ping", host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}