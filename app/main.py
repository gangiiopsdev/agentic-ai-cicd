from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host and all(c.isalnum() or c in ['.', '-'] for c in host) and \
       subprocess.call(["ping", host], shell=False, capture_output=True, text=True) == 0:
        return {"status": "completed", "output": subprocess.getoutput(f'ping {host}').strip()} # Remove leading/trailing whitespace
    return {"status": "failed"}