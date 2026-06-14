from fastapi import FastAPI
import subprocess
def sanitize_input(input):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in input if c in allowed_chars)

app = FastAPI()
def execute_command(cmd):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def is_safe_command(command):
    safe_commands = ['ping']  # List of allowed commands
    if command in safe_commands:
        return True
    else:
        return False

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if is_safe_command('ping'):
        cmd = ["ping", sanitized_host]
        result = execute_command(cmd)
        return {"status": "completed", "output": result}
    else:
        return {"status": "error", "message": "Invalid command"}