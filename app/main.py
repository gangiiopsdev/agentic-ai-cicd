from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def execute_command(command_parts):
    try:
        result = subprocess.run([quote(part) for part in command_parts], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_input(host):
    # Implement input validation logic here
    if not host.isdigit():
        raise ValueError('Invalid input')

@app.get("/ping")
def ping(host: str):
    try:
        validate_input(host)
        command_parts = ['ping', quote(host)]
        output = execute_command(command_parts)
        return {'status': 'completed', 'output': output}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}