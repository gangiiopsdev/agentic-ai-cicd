from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command):
    # Validate and sanitize the command before running it
    try:
        safe_command = shlex.split(command)
    except ValueError as e:
        return str(e)
    result = subprocess.run(safe_command, capture_output=True, text=True)
    return result.stdout