from fastapi import FastAPI
import subprocess
from shlex import quote

def execute_safe_command(command, args):
    safe_args = [quote(arg) for arg in args]
    try:
        result = subprocess.run([command] + safe_args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = 'ping'
    args = [host]
    output = execute_safe_command(command, args)
    return {'status': 'completed', 'output': output}