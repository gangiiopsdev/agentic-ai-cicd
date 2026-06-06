from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and input sanitization
    if not host.isalnum():
        return {"status": "error", "error": "Invalid hostname"}
    try:
        result = subprocess.run(["ping", host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}  # Capture and return output for better visibility
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}  # Handle errors gracefully