from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if not host:
        return {"status": "error", "message": "Host parameter is required"}
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}