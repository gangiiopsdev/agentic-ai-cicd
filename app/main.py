from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use a list instead of a string for the command to avoid shell injection
        subprocess.call(["ping", host])
        return {"status": "completed"}
    except Exception as e:
        return {"status": "error", "message": str(e)}