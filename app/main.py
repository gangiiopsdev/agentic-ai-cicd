from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.run instead of subprocess.call
    subprocess.run(['ping', host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(subprocess.escape_shell(host))  # Escape user input to prevent shell injection
    return {"status": "completed"}