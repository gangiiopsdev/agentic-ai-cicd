from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.call(["ping", host], timeout=10)
    except Exception as e:
        return {"status": "failed", "error": str(e)}
    else:
        return {"status": "completed"}