from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if not host.isalnum():
        return {"error": "Invalid input"}
    subprocess.call(f'ping {host}', shell=False)

    return {"status": "completed"}