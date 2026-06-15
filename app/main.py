from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.startswith('192.168.') or host.startswith('localhost'):  # Add more allowed hosts as needed
        subprocess.call(['ping', host])
    else:
        return {"error": "Unauthorized host"}

    return {"status": "completed"}