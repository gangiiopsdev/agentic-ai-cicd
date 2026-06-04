from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Sanitize the input to prevent command injection
    sanitized_host = subprocess.quote(host)
    subprocess.run(['ping', '-c', '1', sanitized_host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    sanitized_host = subprocess.quote(host)
    subprocess.run(['ping', '-c', '1', sanitized_host], check=True)
    return {"status": "completed"}