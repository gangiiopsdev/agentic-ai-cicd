from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use the check_output method to avoid shell=True and command injection
        result = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": result}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}