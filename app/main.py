from fastapi import FastAPI
import subprocess
import shlex
def run_command(command):
    # Validate and sanitize the command input
    try:
        args = shlex.split(' '.join(command))
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'