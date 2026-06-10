from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and executable=None
    subprocess.run(['ping', host], check=True, shell=False, executable=None)

@app.get("/ping")
def ping_endpoint(host: str):
    return await ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}