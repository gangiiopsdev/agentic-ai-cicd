from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not is_valid_host(host):
        return {"error": "Invalid host"}

    try:
        subprocess.call(['ping', host])
    except Exception as e:
        return {"error": str(e)}

    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Implement validation logic for the host input
    return all(char.isalnum() or char in '.-:' for char in host)