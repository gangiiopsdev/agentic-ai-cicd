from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Using subprocess.run instead of subprocess.call
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Using a safe implementation of ping
    output = safe_ping(host)
    return {"status": "completed", "output": output}