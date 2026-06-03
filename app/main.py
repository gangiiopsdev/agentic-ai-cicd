from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with proper sanitization
    safe_host = shlex.quote(host)
    subprocess.run(['ping', safe_host], check=True, capture_output=True)
    return {"status": "completed"}