from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Using a safe method to execute the command
        subprocess.call(['ping', host], shell=False)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "error", "message": str(e)}