from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/)")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with additional validation and error handling
    try:
        if not re.match(r'^[a-zA-Z0-9.-_]+$', host):
            raise ValueError("Invalid hostname")
        subprocess.run(['ping', host], check=True, shell=False)
    except (subprocess.CalledProcessError, ValueError) as e:
        return {"status": "error", "message": str(e)}
    return {"status": "completed"}