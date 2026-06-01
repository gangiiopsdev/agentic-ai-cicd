from fastapi import FastAPI
import subprocess
def run_safe_command(command: str):
    args = command.split()
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_command = f'ping {host}'
    run_safe_command(safe_command)
    return {"status": "completed"}