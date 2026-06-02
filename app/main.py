from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not host or len(host) > 255 or any(char in host for char in ' 	<>|&*?^()[]{}$\'):
        return {"status": "error", "message": "Invalid host parameter"}
    # Secure implementation using subprocess.run with list of arguments
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}