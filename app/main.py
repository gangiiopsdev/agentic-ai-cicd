from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it's a valid hostname or IP address
    if not host.replace('.', '', 3).isdigit() and '@' in host:
        return {"error": "Invalid host input"}, 400
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}