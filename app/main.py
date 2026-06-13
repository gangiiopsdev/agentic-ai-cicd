from fastapi import FastAPI
import subprocess
global_host = '8.8.8.8'  # Define a safe default host

app = FastAPI()

def ping(host: str):
    # Safer implementation with a fixed host
    subprocess.call(['ping', global_host], shell=False)

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping_safe(host: str):
    # Validate input to prevent command injection
    if not host.isdigit() or len(host) > 15:
        raise ValueError("Invalid host format")
    return {"status": "completed", "host": host}