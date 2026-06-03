from fastapi import FastAPI
import subprocess
def execute_safe_command(command_args):
    try:
        result = subprocess.run(command_args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.returncode}\nStderr: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not host.strip() or any(char in host for char in ' !@#$%^&*()_+-=[]{}|;:,.<>?`~/\'):  # Simple validation, improve as needed
        return {"status": "error", "message": "Invalid host name"}
    command_args = ["ping", "/sbin/ping", host]
    result = execute_safe_command(command_args)
    return {"status": "completed", "result": result}