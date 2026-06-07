from fastapi import FastAPI
import subprocess
from subprocess import run

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run
    result = run(['ping', host], capture_output=True, text=True, shell=False)
    return {"status": "completed", "output": result.stdout}