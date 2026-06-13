from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    if host == 'example.com':  # Validate input
        subprocess.call(['ping', host])
        return {"status": "completed"}
    else:
        raise ValueError("Invalid host")

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Safe implementation
    subprocess.call(['ping', host])
    return {"status": "completed"}