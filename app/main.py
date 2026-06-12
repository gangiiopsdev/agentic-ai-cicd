from fastapi import FastAPI
import subprocess
import shlex
def run_safe_command(command):
    try:
        result = subprocess.run(shlex.split(command), check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.output}'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = host.strip()  # Remove any leading/trailing whitespace
    if all(c.isalnum() or c in '-.' for c in safe_host):  # Allow alphanumeric characters, hyphens, and dots
        return {'output': run_safe_command(f'ping {safe_host}')}  # Fixed the command injection vulnerability
    else:
        return {'error': 'Invalid host'}