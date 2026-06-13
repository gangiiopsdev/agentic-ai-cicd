from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    allowed_hosts = ['google.com', 'example.com']  # Example of allowed hosts
    if host in allowed_hosts:
        subprocess.run(["ping", host], check=True)
        return {"status": "completed"}
    else:
        return {"error": "Host not allowed"}