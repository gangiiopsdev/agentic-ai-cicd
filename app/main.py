from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Safe implementation using subprocess.run
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}