from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation using subprocess.run with shell=False and check=True
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_host(host: str):
    # Safer implementation using subprocess.run with shell=False and check=True
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}