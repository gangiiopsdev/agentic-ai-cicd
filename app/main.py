from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"status": "error", "message": "Invalid input"}
    try:
        subprocess.run(['ping', host], check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}