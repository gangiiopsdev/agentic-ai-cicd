from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Use a list instead of a string for the command and arguments
    subprocess.call(['ping', host])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}