from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.strip() not in ['localhost', '127.0.0.1']:
        return {"error": "Invalid host"}, 400
    subprocess.run(['ping', '-c', '5', host], check=True, timeout=5)
    return {"status": "completed"}