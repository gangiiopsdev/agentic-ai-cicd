from fastapi import FastAPI
import subprocess
def safe_command(command):
    return [arg.replace(';', ' ') for arg in command.split()]

app = FastAPI()
def sanitize_input(input_string):
    # Implement proper sanitization logic here
    return ''.join(char for char in input_string if char.isalnum())

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(safe_command(f'ping {sanitized_host}'))
    return {"status": "completed"}