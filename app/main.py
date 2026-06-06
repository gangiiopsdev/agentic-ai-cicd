from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or len(host) > 10:
        raise ValueError("Invalid host name")
    # Secure implementation using a list of arguments and validating input
    subprocess.run(['ping', '--'], check=True, args=[host])
    return {"status": "completed"}