from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using list of arguments instead of shell=True
    subprocess.call(['ping', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)  # Directly pass host to prevent shell injection
    return {"status": "completed"}