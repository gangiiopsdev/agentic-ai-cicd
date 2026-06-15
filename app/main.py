from fastapi import FastAPI
import subprocess
git
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}