from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using check=True to handle errors gracefully
    try:
        subprocess.run(['ping', '-c', '1', host], check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

def home():
    return {"message": "Agentic Self-Healing Pipeline"}