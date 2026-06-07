from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation and absolute path
    if host.strip() == 'localhost' or host.strip() == '127.0.0.1':
        subprocess.call(["/bin/ping", host])
        return {"status": "completed"}
    else:
        return {"status": "denied", "message": "Invalid host"}