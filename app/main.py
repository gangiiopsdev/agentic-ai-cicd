from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host or len(host) > 255 or not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError('Invalid hostname')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    args = ['ping', host]
    # Use subprocess.run instead of subprocess.call to capture output and handle errors more safely
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {"status": "completed", "output": result.stdout}