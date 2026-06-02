from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        return {"error": "Invalid hostname"}, 400
    subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed"}