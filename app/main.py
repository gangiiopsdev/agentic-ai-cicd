from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run instead of subprocess.call
    subprocess.run(['ping', host], capture_output=True, text=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Ensure the input is properly sanitized
    if not host.isalnum():
        raise ValueError("Invalid input for hostname")
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": result.stdout}