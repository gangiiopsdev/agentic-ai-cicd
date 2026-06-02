from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isdigit() or e in ['.', '-', '_'])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isdigit() or len(host) > 3:
        return {"status": "error", "message": "Invalid input"}
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping -c 1 {sanitized_host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}