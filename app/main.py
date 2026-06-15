from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Input validation and sanitization
    if not host.isalnum() or len(host) > 255:
        return {"error": "Invalid input"}, 400
    subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed"}