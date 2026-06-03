from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_!@#$%^&*()+=[]{};:,.<>?/\|`~ '  # Define allowed characters
    sanitized = ''.join(c for c in user_input if c in allowed_chars)
    return sanitized

def execute_command(command, *args):
    try:
        output = subprocess.check_output([command] + list(args), stderr=subprocess.STDOUT)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return e.output.decode()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    output = execute_command('ping', sanitized_host)
    return {'status': 'completed', 'output': output}