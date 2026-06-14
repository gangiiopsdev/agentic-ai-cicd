from fastapi import FastAPI
import subprocess
from shlex import quote
generate_ping_command = lambda host: f'ping {quote(host)}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run instead of subprocess.call
    result = subprocess.run(generate_ping_command(host), shell=False, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}