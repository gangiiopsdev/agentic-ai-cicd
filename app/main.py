from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/" )
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and list of arguments
    if not host.isdigit() or len(host.split('.')) != 4:
        return {"status": "error", "message": "Invalid IP address"}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}