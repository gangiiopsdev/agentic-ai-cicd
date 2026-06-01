from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Use subprocess.run instead of subprocess.call and avoid shell=True
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout,

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Use the safe_ping function to avoid command injection
    status = safe_ping(host)
    return {"status": status}