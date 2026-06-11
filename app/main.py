from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    try:
        subprocess.check_call(['ping', host], timeout=10)
    except subprocess.CalledProcessError as e:
        return {"error": f'Ping failed with error: {e}'}
    return {"status": "completed"}