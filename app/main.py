from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Fixed implementation using a full executable path and avoiding shell=True
    subprocess.call(["/bin/ping", host])
    return {"status": "completed"}