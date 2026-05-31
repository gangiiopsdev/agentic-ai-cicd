from fastapi import FastAPI
import subprocess
import shlex
def execute_command(command: str):
    try:
        args = shlex.split(command)
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Command failed with exit code {e.returncode}: {e.stderr}"

global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    output = execute_command(command)
    return {"status": "completed", "output": output}