from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation with argument validation and sanitization
    if not all(c.isalnum() or c in '._-' for c in host):
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', host], check=True, text=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}