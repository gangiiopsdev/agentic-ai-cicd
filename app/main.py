from fastapi import FastAPI
import subprocess
def execute_ping(host):
    # Validate and sanitize host input
    if not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError('Invalid host')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)