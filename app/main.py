from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    # Ensure input is validated and sanitized
    if not host.isalnum():
        raise ValueError("Invalid input")
    # Use subprocess.run instead of subprocess.call for better security
    result = subprocess.run(['ping', host], shell=False, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}