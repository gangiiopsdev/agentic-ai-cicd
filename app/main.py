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
        subprocess.run([Ping().command, '127.0.0.1'], check=True, shell=False)  # Fixed: Use subprocess.run and add check=True
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e), "status": "failed"}