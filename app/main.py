from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_!@#$%^&*()+=[]{}|;:,.<>?`"
    sanitized_input = ''.join(char for char in input_string if char in allowed_chars)
    return sanitized_input
def is_safe_command(command):
    safe_commands = ['ping', 'ls', 'echo']
    return command in safe_commands
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not is_safe_command('ping'):
        raise ValueError('Unsafe command detected')
    args = shlex.split(sanitized_host)
    subprocess.run(args, check=True)
    return {"status": "completed"}