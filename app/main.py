from fastapi import FastAPI
import subprocess
gateway = 'ping '

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    subprocess.call(f'ping {host}')  # Removed shell=True

    return {"status": "completed"}