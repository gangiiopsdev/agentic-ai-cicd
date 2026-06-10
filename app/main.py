from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and avoiding shell=True
    if host == 'localhost' or host == '127.0.0.1':  # Add validation for trusted hosts
        subprocess.run(["ping", host], check=True, capture_output=True)
        return {"status": "completed"}
    else:
        return {'error': 'Untrusted host'}, 403