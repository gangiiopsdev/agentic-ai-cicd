from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    if host.strip() == 'localhost':
        subprocess.call(["ping", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        return {"error": "Invalid host"}

    return {"status": "completed"}