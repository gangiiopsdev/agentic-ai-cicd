from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/)")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        sanitized_host = re.sub(r'[^a-zA-Z0-9.-_]', '', host)
        subprocess.run(['ping', sanitized_host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}
    return {"status": "completed"}