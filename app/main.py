from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and full path
    if host in ['google.com', 'example.com']:  # Add allowed hosts here
        subprocess.call(['/usr/bin/ping', '-c', '4', host])
    else:
        return {"error": "Host not allowed"}

    return {"status": "completed"}