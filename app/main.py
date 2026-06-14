from fastapi import FastAPI
import subprocess
def execute_command(command):
    # Validate and sanitize the input to prevent command injection
    allowed_commands = ['ping']
    if command.split()[0] in allowed_commands:
        return subprocess.run(command, shell=False, check=True)
    else:
        raise ValueError('Invalid command')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent injection
    sanitized_host = ''.join(c for c in host if c.isalnum() or c in ['-', '.', ':'])
    command = f'ping {sanitized_host}'
    result = execute_command(command)
    return {"status": "completed", "result": result}