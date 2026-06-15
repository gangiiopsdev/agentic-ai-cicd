from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if host.strip() and host.isalnum():  # Simple alphanumeric check
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid input"}