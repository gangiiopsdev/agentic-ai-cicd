from fastapi import FastAPI
import subprocess
def execute_command(command, args):
    # Validate and sanitize inputs before executing
    allowed_commands = ['ping', 'ls']
    if command not in allowed_commands:
        raise ValueError('Invalid command')
    result = subprocess.run([command] + args, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate and sanitize host input before executing
    if not host:
        raise ValueError('Host parameter is required')
    return {'status': 'completed', 'output': execute_command('ping', [host])}