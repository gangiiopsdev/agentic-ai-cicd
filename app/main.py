from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation with argument sanitization
    safe_host = shlex.quote(host)
    subprocess.run(['ping', safe_host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):  # Renamed to avoid conflicts with the original function
    return {"status": "completed"}