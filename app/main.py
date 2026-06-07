from fastapi import FastAPI
import subprocess
def execute_command(command):
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isalnum():
        raise ValueError("Invalid host input")
    command = ["ping", host]
    result = execute_command(command)
    return {"status": "completed", "output": result}