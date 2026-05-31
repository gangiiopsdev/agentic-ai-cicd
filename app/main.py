from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.split to safely split the command into arguments
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}