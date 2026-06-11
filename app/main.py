from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        subprocess.call(['ping', host], check=True)
        return {"status": "completed", "details": "Ping successful"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "details": str(e)}