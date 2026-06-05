from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host:
        return {"error": "Host parameter is required"}
    # Safe implementation using subprocess.call with shell=False
    args = ["ping", host]
    subprocess.call(args)
    return {"status": "completed"}