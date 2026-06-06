from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use subprocess.run instead and avoid shell=True
    ping_command = ['ping', host]
    result = subprocess.run(ping_command, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    status = safe_ping(host)
    return {"status": "completed", "output": status}