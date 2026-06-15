from fastapi import FastAPI
import shlex
import subprocess

def safe_subprocess(command):
    try:
        # Validate and sanitize the command
        if not command.isalnum():
            raise ValueError('Unsafe input detected')
        args = shlex.split(command)
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Command failed: {e.stderr}'

app = FastAPI()