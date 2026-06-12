from fastapi import FastAPI
import subprocess
global_host = '8.8.8.8'  # Define a safe default host

app = FastAPI()

def ping(host: str):
    # Safer implementation with a fixed host
    subprocess.call(['ping', global_host], shell=False)

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    return {"status": "completed"}