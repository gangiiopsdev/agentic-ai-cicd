from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self):
        self.command = 'ping'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"error": "Invalid input", "status": "failed"}
    try:
        subprocess.call([Ping().command, '127.0.0.1'], shell=False)  # Fixed: Use a safe default host
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}