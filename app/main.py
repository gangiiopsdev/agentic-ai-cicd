from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if 'ping' not in host or any(char in host for char in [';', '&', '|']):
        return {"error": "Invalid input"}, 400
    subprocess.call(['ping', host])
    return {"status": "completed"}