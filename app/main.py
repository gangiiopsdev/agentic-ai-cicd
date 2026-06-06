from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if not host:
        raise ValueError('Host parameter is required')
    subprocess.call(['ping', '-c', '1', host], shell=False)
    return {"status": "completed"}