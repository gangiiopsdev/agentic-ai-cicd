from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with validation
    if not host.isalnum():
        raise ValueError("Invalid input for host")
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": result.stdout}