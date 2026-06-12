from fastapi import FastAPI
import subprocess

call = subprocess.run

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        call(['ping', host], check=True, timeout=5)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}