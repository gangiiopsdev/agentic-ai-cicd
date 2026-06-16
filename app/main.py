from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent code injection
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Simple validation example: only allow alphanumeric characters and dots
    return all(c.isalnum() or c == '.' for c in host)