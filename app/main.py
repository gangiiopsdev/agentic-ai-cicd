from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation using subprocess.run with shell=False and avoiding shell=True
    subprocess.run(['ping', host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping(host)
    return {"status": "completed"}