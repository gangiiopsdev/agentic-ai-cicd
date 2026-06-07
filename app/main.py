from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent command injection
    if not host.isdigit() or len(host) > 15:
        return {"error": "Invalid host"}, 400
    subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True)
    return {"status": "completed"}