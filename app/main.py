from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    subprocess.call(['ping', host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    safe_ping(host)

    return {"status": "completed"}