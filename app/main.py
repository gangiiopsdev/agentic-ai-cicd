from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using Popen
    args = ['ping', host]
    subprocess.Popen(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}