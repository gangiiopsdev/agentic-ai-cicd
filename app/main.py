from fastapi import FastAPI
import subprocess
def execute_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or '.' in host:
        return {"status": "error", "output": "Invalid host"}
    command = ['ping', host]
    result = execute_command(command)
    return {"status": "completed", "output": result}