from fastapi import FastAPI
import subprocess
def execute_safe_ping(host):
    # Safe implementation using args instead of shell=True
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    execute_safe_ping(host)
    return {"status": "completed"}