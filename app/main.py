from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)

@app.get="/"
async def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
async def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}