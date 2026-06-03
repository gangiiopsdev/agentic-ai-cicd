from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isdigit() or int(host) < 1 or int(host) > 254:
        return {"status": "error", "message": "Invalid host address"}
    safe_host = subprocess.quote(host)
    subprocess.run(['ping', '-c', '1', safe_host], check=True)
    return {"status": "completed"}