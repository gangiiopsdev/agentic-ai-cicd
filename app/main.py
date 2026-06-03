from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use a list for the command to avoid shell injection
        subprocess.call(["ping", host], shell=False)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500