from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run with proper sanitization of host input
    subprocess.run(['ping', '-c', '1', '--', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping(host)
    return {"status": "completed"}