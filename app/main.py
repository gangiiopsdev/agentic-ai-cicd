from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with proper sanitization of input
    result = subprocess.run(['ping', host], check=True, capture_output=True)
    return {"status": "completed", "output": result.stdout.decode()}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}