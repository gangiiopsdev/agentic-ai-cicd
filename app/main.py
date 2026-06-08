from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"")
def root():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if not host.strip():
        raise ValueError('Host parameter is required')
    subprocess.run(['ping', host], check=True, shell=False)
    return {"status": "completed"}