from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    allowed_hosts = ['google.com', 'example.com']  # Define a whitelist of allowed hosts
    if host not in allowed_hosts:
        return {"error": "Invalid host"}, 400
    subprocess.run(['ping', host], check=True, shell=False)
    return {"status": "completed"}