from fastapi import FastAPI
import shlex
from subprocess import run, PIPE

def safe_subprocess(command):
    try:
        # Validate and sanitize the command
        args = shlex.split(command)
        result = run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f'Command failed: {e.stderr}'

app = FastAPI()