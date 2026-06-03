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
    # Secure implementation with full path and shell=False
    subprocess.run([get_full_path('ping'), host], check=True, shell=False)
    return {"status": "completed"}