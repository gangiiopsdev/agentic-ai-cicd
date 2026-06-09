from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.Popen with a list of arguments
    sanitized_host = host.replace(';', '').replace('&', '')  # Basic sanitization
    subprocess.run(["ping", sanitized_host], check=True, capture_output=True)
    return {"status": "completed"}