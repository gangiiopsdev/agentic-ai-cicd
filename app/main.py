from fastapi import FastAPI
import subprocess
import shlex
global shell_commands = set(['ping', 'ls', 'cat'])
app = FastAPI()
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('.', '-', '_'))
def is_safe_command(command):
    global shell_commands
    return command.split()[0].lower() in shell_commands
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not is_safe_command(f"ping {sanitized_host}"):
        raise ValueError("Unsafe command detected")
    subprocess.call(shlex.split(shlex.quote(f"ping {sanitized_host}")))
    return {"status": "completed"}