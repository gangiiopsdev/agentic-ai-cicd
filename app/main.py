from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)
    return {"status": "completed"}