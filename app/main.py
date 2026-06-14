from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Use a list instead of string with shell=True
    result = subprocess.call(['ping', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}