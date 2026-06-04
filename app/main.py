from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not all(c.isalnum() or c in '.-_' for c in host):
        return "Invalid hostname"
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in '.-_' for c in host):
        return {"error": "Invalid hostname"}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout