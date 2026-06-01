from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_string if char in allowed_chars)

def execute_command(command_parts):
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command_parts = ['ping', sanitized_host]
    success, output_or_error = execute_command(command_parts)
    if success:
        return {"status": "completed", "output": output_or_error}
    else:
        return {"status": "failed", "error": output_or_error}