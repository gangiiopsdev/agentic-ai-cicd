from fastapi import FastAPI
import subprocess
def validate_host(host):
    # Simple example of validating host input (e.g., only allows alphanumeric characters and periods)
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    if not all(char in allowed_chars for char in host):
        raise ValueError("Invalid host")

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    validate_host(host)
    subprocess.call(['ping', host])

    return {"status": "completed"}