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
        subprocess.call(["ping", host])
    except Exception as e:
        return {"error": str(e), "status": "failed"}

    return {"status": "completed"}