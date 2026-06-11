from fastapi import FastAPI
import subprocess
def sanitize_input(input):
    return ''.join(c for c in input if c.isalnum() or c in '-_.')

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', sanitized_host], check=True, capture_output=True)
    return {"status": "completed"}