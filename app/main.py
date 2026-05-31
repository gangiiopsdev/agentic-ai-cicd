from fastapi import FastAPI
import subprocess
import shlex
def execute_command(command: str):
    args = shlex.split(command)
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return result.stdout

global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping -c 1 {host}'
    output = execute_command(command)
    return {"status": "completed", "output": output}