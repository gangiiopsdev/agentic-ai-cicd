from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isnumeric() or int(host) < 1 or int(host) > 255:
        return {"error": "Invalid host value"}
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}