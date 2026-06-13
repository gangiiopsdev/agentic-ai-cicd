from fastapi import FastAPI
import subprocess

def validate_and_sanitize_input(command: str) -> bool:
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')
    return all(char in allowed_chars for char in command)

def execute_command(command: str):
    if not validate_and_sanitize_input(command):
        return {'status': 'error', 'output': 'Invalid argument'}
    result = subprocess.run(command.split(), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if not validate_and_sanitize_input(host) or 'ping' not in host:
        return {'status': 'error', 'output': 'Invalid host'}
    command = ['ping', host]
    return execute_command(' '.join(command))