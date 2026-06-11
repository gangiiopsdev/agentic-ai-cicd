from fastapi import FastAPI
import subprocess
import shlex
def run_safe_command(command):
    try:
        result = subprocess.run(['ping', *shlex.split(command)], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.output}__module__', '__name__', '__qualname__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__'])

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = host.strip()  # Remove any leading/trailing whitespace
    if all(c.isalnum() or c in '-.' for c in safe_host):  # Allow alphanumeric characters, hyphens, and dots
        return {'output': run_safe_command(f'ping {safe_host}__module__', '__name__', '__qualname__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__'])
    else:
        return {'error': 'Invalid host'}