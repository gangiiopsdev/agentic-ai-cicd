from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    # Validate and sanitize input
    if not host.isalnum() or '.' in host:
        return {"error": "Invalid host name"}
    return run_command(command)