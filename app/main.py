from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation and absolute path
    if host.strip() in ['localhost', '127.0.0.1']:
        subprocess.run(['/bin/ping', host], check=True, capture_output=True)
    return {"status": "completed"}