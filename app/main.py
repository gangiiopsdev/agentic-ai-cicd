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
        # Secure implementation using subprocess.run with absolute path and validation
        if host in ['localhost', '127.0.0.1']:
            result = subprocess.run(['/bin/ping', host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        else:
            return {"status": "failed", "error": "Untrusted input detected."}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}