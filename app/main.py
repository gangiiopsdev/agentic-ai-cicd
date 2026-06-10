from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent shell injection
    if not host.isalnum() or len(host) > 64:
        return {"error": "Invalid host input"}, 400

    args = ['ping', host]
    subprocess.call(args)

    return {"status": "completed"}