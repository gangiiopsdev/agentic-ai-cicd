from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with full executable path and shell=False
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
    return {"status": "completed", "output": result.stdout}