from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it's safe for pinging
    if not host.isalnum() or '..' in host:
        return {"error": "Invalid host name"}
    try:
        subprocess.run(['ping', host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
    return {"status": "completed"}