from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    safe_string = ''.join(c for c in input_string if c.isalnum() or c in ['.', '-', '_', ' ', '@', ':'])
    return safe_string

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    safe_host = sanitize_input(host)
    subprocess.call(["ping", safe_host])
    return {"status": "completed"}