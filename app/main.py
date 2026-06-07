from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to avoid command injection
    allowed_hosts = ['example.com', 'test.com']  # Example list of allowed hosts
    if host not in allowed_hosts:
        return {"error": "Unauthorized host"}, 403

    # Safer implementation
    subprocess.run(['ping', host], check=True)

    return {"status": "completed"}