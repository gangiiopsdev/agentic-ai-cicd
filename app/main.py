from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    try:
        subprocess.call(['ping', host], shell=False)
    except Exception as e:
        return {"error": str(e)}, 500

    return {"status": "completed"}