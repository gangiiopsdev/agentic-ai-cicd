from fastapi import FastAPI
import subprocess
def execute_safe_command(command: str):
    # Execute command safely without using shell=True
    subprocess.run(command.split(), check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    execute_safe_command(f"ping {host}")
    return {"status": "completed"}