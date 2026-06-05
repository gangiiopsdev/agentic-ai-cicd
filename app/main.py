from fastapi import FastAPI
import subprocess
def escape_command(command):
    return [arg.strip() for arg in command.split()]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.call(escape_command(f'ping -c 1 {host}'), shell=True)  # Use 'shell=True' for proper command execution, but this is still risky.
    except Exception as e:
        return {"error": str(e)}
    return {"status": "completed"}