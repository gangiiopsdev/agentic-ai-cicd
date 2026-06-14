from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    args = ["ping", host]
    subprocess.call(args)

    return {"status": "completed"}