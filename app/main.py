from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host and all(c.isalnum() or c in ['.', '-'] for c in host):
        subprocess.run(["ping", host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        raise ValueError("Invalid host name")

    return {"status": "completed"}