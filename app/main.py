from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_safe_command(command: str):
    args = command.split()
    subprocess.run(args, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    execute_safe_command(f"ping {host}")
    return {"status": "completed"}