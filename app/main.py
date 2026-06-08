from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    return ''.join(c for c in user_input if c.isalnum() or c in ['-', '.', '_', ' ', '/'])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        raise ValueError("Invalid host input")
    subprocess.call(f"ping {sanitized_host}")
    return {"status": "completed"}