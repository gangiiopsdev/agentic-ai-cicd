from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with a list of arguments and shell=False
    sanitized_host = host.replace(';', '').replace('&', '')  # Basic sanitization
    result = subprocess.run(["ping", sanitized_host], check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}