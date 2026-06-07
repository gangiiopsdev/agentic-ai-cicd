from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safer implementation using subprocess.run and list of arguments
    subprocess.run(['ping', host], check=True)
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation using subprocess.run and list of arguments
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}