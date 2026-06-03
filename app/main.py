from fastapi import FastAPI
import subprocess
import os
import shlex

global app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate input to prevent command injection using shlex.quote
        safe_host = shlex.quote(host)
        result = subprocess.check_output(["ping", safe_host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": result}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}