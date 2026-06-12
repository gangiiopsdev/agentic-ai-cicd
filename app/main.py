from fastapi import FastAPI
import subprocess
def execute_command(command):
    # Validate and sanitize the input to prevent command injection
    allowed_commands = ['ping']
    if command.split()[0] in allowed_commands:
        return subprocess.call(command, shell=False)
    else:
        raise ValueError('Invalid command')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    result = execute_command(command)
    return {"status": "completed", "result": result}