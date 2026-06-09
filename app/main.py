from fastapi import FastAPI
import subprocess
def execute_safe_command(command):
    args = command.split()
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_command = f'ping -c 1 {host}'
    execute_safe_command(safe_command)