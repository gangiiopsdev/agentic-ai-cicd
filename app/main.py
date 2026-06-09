from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host or ' ' in host:
        raise ValueError("Invalid host name")
    subprocess.run(['ping', host], check=True, shell=False)
    return {"status": "completed"}