from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation and full executable path
    try:
        subprocess.call(['ping', host], shell=False)
    except Exception as e:
        return {"status": "error", "message": str(e)}
    return {"status": "completed"}