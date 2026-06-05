from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

def is_safe_hostname(hostname):
    # Simple check for safe hostname characters
    return all(c.isalnum() or c in ['-', '.', '_'] for c in hostname)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_hostname(host):
        return {"status": "failed", "error": "Invalid hostname"}
    try:
        result = subprocess.run(["ping", host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}