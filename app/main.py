from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and args, validating input
    safe_host = shlex.quote(host)
    result = subprocess.run(['ping', safe_host], check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}