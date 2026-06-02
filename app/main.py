from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate input to prevent command injection
        if ' ' in host or '\' in host or '"' in host or '>' in host or '<' in host:
            raise ValueError('Invalid input')
        result = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": result}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}