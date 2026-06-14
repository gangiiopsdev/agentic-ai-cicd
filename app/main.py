from fastapi import FastAPI
import subprocess
def safe_subprocess_call(command: str, args: list, timeout=10):
    allowed_commands = ['ping']
    if command not in allowed_commands:
        raise ValueError(f'Command {command} is not allowed')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output([command, host], stderr=subprocess.STDOUT, timeout=timeout)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}