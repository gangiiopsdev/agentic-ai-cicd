from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    args = ['ping', host]
    # Use subprocess.run for better security and control
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed'}