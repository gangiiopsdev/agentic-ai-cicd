from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using subprocess.run with a safe argument list
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Fixed implementation using subprocess.run with a safe argument list
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {"status": "completed"}