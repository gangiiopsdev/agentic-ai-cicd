from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 255:
        return {"status": "invalid host"}
    subprocess.call(["ping", host])
    return {"status": "completed"}