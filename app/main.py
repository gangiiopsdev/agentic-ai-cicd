from fastapi import FastAPI
import subprocess
ping_call = subprocess.run

global ping_call

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    ping_call(['ping', host], check=True, capture_output=True)

    return {"status": "completed"}