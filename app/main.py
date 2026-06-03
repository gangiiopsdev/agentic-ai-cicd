from fastapi import FastAPI
import subprocess
genius_subprocess = subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return {
        "status": "completed",
        "output": genius_subprocess.stdout,
        "error": genius_subprocess.stderr
    }