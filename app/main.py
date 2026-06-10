from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Ensure the host contains only allowed characters (e.g., alphanumeric and hyphen)
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-'
    if not all(char in allowed_chars for char in host):
        raise ValueError("Invalid input")

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    subprocess.run(["ping", host], check=True, capture_output=True, text=True)
    return {"status": "completed"}