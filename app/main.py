from fastapi import FastAPI
import subprocess
from shlex import quote
def validate_input(host):
    if not host.isdigit():
        raise ValueError('Invalid input')
@app.get("/ping")
def ping(host: str):
    try:
        validate_input(host)
        command_parts = ["ping", quote(host)]  # Use shlex.quote to sanitize the input
        output = execute_command(command_parts)
        return {"status": "completed", "output": output}
    except ValueError as e:
        return {"status": "error", "message": str(e)}
def execute_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)