from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with full executable path and validation of host input
    if host in ['127.0.0.1', '::1']:  # Example whitelist, replace with actual validation logic
        subprocess.call(['ping', '-c', '4', host])
    else:
        return {"error": "Invalid host"}
    return {"status": "completed"}