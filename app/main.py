from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation using subprocess.run with shell=False and properly formatted arguments
    subprocess.run(['ping', host], capture_output=True, text=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation using subprocess.run with shell=False and properly formatted arguments
    subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed"}