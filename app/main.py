from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

# Regular expression to validate host domain
VALID_HOST_PATTERN = re.compile(r'^example\.com$')

def validate_host(host):
    if not VALID_HOST_PATTERN.match(host):
        raise ValueError('Invalid host')

def execute_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command_parts = ['ping', host]
    output = execute_safe_command(command_parts)
    return {'status': 'completed', 'output': output}