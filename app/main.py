from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Use subprocess.run for better control and security
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}