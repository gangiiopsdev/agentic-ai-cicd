from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Using subprocess.run for a safer implementation
    subprocess.run(['ping', host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}