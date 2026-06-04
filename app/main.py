from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        return{"error": "Invalid hostname"}, 400

    # Use subprocess.run with shell=False and capture_output=True
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}