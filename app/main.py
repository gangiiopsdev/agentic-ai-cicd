from fastapi import FastAPI
import shlex
import subprocess
def execute_safe_command(command: str):
    args = shlex.split(command)
    process = subprocess.Popen(args, capture_output=True, text=True, shell=False)
    return process.wait(), process.stdout, process.stderr

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_command = f'ping -c 1 {host}'  # Use a safe command with trusted options
    result_code, stdout, stderr = execute_safe_command(safe_command)
    return {"status": "completed", "stdout": stdout, "stderr": stderr}