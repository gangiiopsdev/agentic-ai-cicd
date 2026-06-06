from fastapi import FastAPI
import subprocess
def execute_command(command):
    return subprocess.run(command.split(), capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    result = execute_command(command)
    return {"status": result.stdout, "stderr": result.stderr}