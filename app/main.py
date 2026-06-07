from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_command(command: str):
    args = shlex.split(command)
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error executing command: {e}'

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Use parameterized queries or whitelisting to prevent command injection
    if host in ['127.0.0.1', '::1']:  # Example whitelist
        command = f'ping {host}'
        output = execute_command(command)
        return {"status": "completed", "output": output}
    else:
        return {"status": "error", "message": "Invalid host"}