from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it is safe
    if not host.isalnum() or '.' in host:
        return {"error": "Invalid host"}, 400

    # Secure implementation
    subprocess.run(['ping', host], check=True)

    return {"status": "completed"}