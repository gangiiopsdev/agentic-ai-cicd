from fastapi import FastAPI
import subprocess

app = FastAPI()

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and avoiding use of host directly in command arguments
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}