from fastapi import FastAPI
import subprocess
good_hosts = {'example.com', 'google.com'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in good_hosts:
        raise ValueError("Invalid host")
    # Secure implementation
    subprocess.run(["ping", host], check=True, capture_output=True, text=True)
    return {"status": "completed"}