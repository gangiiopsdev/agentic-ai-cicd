from fastapi import FastAPI
import subprocess
gimport shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.strip().isalnum() or ' ' in host:
        raise ValueError("Invalid input")
    command_parts = shlex.split(f'ping {shlex.quote(host)}')
    result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}