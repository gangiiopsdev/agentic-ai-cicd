from fastapi import FastAPI
import subprocess

app = FastAPI()

def get_full_path(command):
    # Replace with actual logic to get full path of the command
    return '/usr/bin/' + command

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid hostname")
    subprocess.run([get_full_path('ping'), host], check=True, shell=False)
    return {"status": "completed"}