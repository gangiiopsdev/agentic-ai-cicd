from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    safe_host = shlex.quote(host)
    subprocess.run(['ping', safe_host], check=True)
    return {"status": "completed"}