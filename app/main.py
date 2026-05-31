from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation using subprocess.run()
    subprocess.run(['ping', host], check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation
    if host.isalnum() and len(host) <= 64:
        subprocess.run(['ping', host], check=True)
    else:
        return {"error": "Invalid input"}
    return {"status": "completed"}