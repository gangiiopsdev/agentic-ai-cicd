from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(c for c in input_string if c in allowed_chars)

def shell_safe_command(command_parts):
    command = [shlex.quote(part) for part in command_parts]
    return ' '.join(command)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = shell_safe_command(['ping', sanitized_host])
    subprocess.call(command, shell=True)
    return {"status": "completed"}