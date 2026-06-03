from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent injection attacks
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed"}

# Example validation function
import re
def is_valid_host(hostname: str) -> bool:
    pattern = re.compile(r'^[a-zA-Z0-9-.]+$')
    return bool(pattern.match(hostname))