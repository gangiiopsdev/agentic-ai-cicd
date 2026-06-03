from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        return {"error": "Invalid input"}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": result.stdout}

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run without shell=True
    if not host.isalnum():
        return {"error": "Invalid input"}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": result.stdout}