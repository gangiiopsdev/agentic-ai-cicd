from fastapi import FastAPI
import subprocess
def execute_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout
global app = FastAPI()

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 64:
        raise ValueError("Invalid hostname")
    sanitized_host = subprocess.list2cmdline([host])  # Sanitize the input
    command = ["ping", "-c", "1", sanitized_host]  # Limit the number of pings for security
    result = execute_command(command)
    return {"status": "completed", "output": result}