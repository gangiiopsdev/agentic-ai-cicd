from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call for better security and control over the arguments.
        subprocess.run(["ping", host], check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

    return {"status": "completed"}