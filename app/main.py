from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(input_string):
    return input_string.strip()

async def execute_safe_command(command, *args):
    safe_args = [quote(arg) for arg in args]
    full_command = [command] + list(safe_args)
    try:
        output = subprocess.run(full_command, capture_output=True, text=True, check=True)
        return True, output.stdout
    except subprocess.CalledProcessError as e:
        return False, str(e)

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

def ping(host: str):
    sanitized_host = sanitize_input(host)
    success, output = execute_safe_command('ping', '-c', '1', sanitized_host)
    if success:
        return {"status": "completed", "output": output}
    else:
        return {"status": "failed", "error": output}