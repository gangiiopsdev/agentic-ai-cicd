from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and input sanitization
    if not host.isalnum() or len(host) > 255:
        return {"status": "error", "error": "Invalid hostname"}
    command_parts = shlex.split(f'ping {host}')
    output = execute_command(command_parts)
    return {"status": "completed", "output": output}