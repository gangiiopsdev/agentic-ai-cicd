from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run instead of subprocess.call
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    sanitized_host = subprocess.quote(host)
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}