from fastapi import FastAPI
import subprocess
import shlex
def execute_command(command: str):
    args = shlex.split(command)
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = f'ping {host}'
    execute_command(command)
    return {"status": "completed"}