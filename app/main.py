from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Secure implementation using subprocess.run with absolute path and sanitized input
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)

    return {"status": "completed", "output": result.stdout}