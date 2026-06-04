from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    # Safe implementation using subprocess.run without shell=True
    subprocess.run(['ping', host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    run_ping(host)
    return {"status": "completed"}