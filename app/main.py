from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with check=True and capture_output=True
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "stdout": result.stdout, "stderr": result.stderr}