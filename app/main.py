from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = host.strip().replace(' ', '')  # Sanitize input to avoid spaces and other potential issues
    if safe_host.startswith('-'):  # Prevent starting with an option that could be used for command injection
        return {"error": "Invalid host provided"}
    subprocess.run(['ping', safe_host], check=True)
    return {"status": "completed"}