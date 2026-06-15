from fastapi import FastAPI
import shlex
import subprocess

def safe_subprocess(command):
    # Validate and sanitize the command here
    allowed_commands = ['ls', 'pwd']  # Example of allowed commands
    if command in allowed_commands:
        args = shlex.split(command)
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    else:
        return 'Command not allowed'

app = FastAPI()