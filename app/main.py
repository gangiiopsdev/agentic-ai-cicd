from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command, *args):
    if not isinstance(command, str) or not command.isalnum() and '-' not in command:
        raise ValueError("Invalid command")
    return subprocess.run([command] + list(args), capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() and '-' not in host:
        raise ValueError("Invalid hostname")
    result = execute_command('ping', host)
    return {'status': 'completed', 'output': result.stdout}