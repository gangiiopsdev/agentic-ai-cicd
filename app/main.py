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

# Add input validation for host parameter
def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.example.com']  # Define allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Host is not allowed')
    safe_command = f'ping -c 1 {host}'  # Use a safe command with trusted options
    result_code, stdout, stderr = execute_safe_command(safe_command)
    return {"status": "completed", "stdout": stdout, "stderr": stderr}