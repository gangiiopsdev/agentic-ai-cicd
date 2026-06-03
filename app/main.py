from fastapi import FastAPI
import subprocess
gimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_host = subprocess.quote(host)
    args = ['ping', safe_host]
    subprocess.run(args, check=True)

    return {"status": "completed"}