from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Use subprocess.run with args to avoid shell injection
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Using safe_ping function to avoid command injection
    result = safe_ping(host)
    return {"status": "completed", "output": result}