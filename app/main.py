from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.run(['ping', host], check=True, capture_output=True)
        return {"status": "completed", "output": subprocess.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": e.stderr.decode()}