from fastapi import FastAPI
import subprocess
def validate_input(value):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    if not all(char in allowed_chars for char in value):
        raise ValueError("Invalid input")

app = FastAPI()
def execute_command(command_parts):
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    validate_input(host)
    command_parts = ['ping', host]
    return execute_command(command_parts)