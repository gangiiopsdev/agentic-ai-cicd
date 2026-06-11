from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent injection attacks
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True, shell=False)
    return {"status": "completed"}

# Function to validate the host input
def is_valid_host(host: str) -> bool:
    # Add your validation logic here
    return host.strip() and not any(char in host for char in [';', '&', '|', '<', '>', '`'])