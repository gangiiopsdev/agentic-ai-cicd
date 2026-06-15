from fastapi import FastAPI
import subprocess
gimport shlex

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 50:
        return {"status": "error", "output": "Invalid host"}
    command_parts = shlex.split(f'ping -c 4 {host}')
    result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}