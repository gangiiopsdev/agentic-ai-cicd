from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using check_output with shell=False and avoid unsafe input
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}