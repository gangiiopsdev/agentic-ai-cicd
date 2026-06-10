from fastapi import FastAPI
import subprocess
def execute_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout
global app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 64:
        raise ValueError("Invalid hostname")
    command = ["ping", host]
    result = execute_command(command)
    return {"status": "completed", "output": result}