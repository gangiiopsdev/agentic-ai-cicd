from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Fixed implementation with input validation
    if not host.strip() or len(host) > 100:
        return {"error": "Invalid input"}
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}