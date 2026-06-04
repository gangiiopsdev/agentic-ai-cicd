from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid input")
    # Use a whitelist of allowed hosts or validate the host format
    if host not in ['example.com', 'another-example.com']:
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}, 400