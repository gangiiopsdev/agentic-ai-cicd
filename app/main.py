from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c.isdigit() or c in [".", "-"])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping -c 1 {sanitized_host}')
    subprocess.run(args, check=True, capture_output=True)
    return {"status": "completed"}