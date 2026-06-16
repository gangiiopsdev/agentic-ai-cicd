from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    # Simple validation to avoid command injection
    if any(char in input_str for char in [';', '|', '&', '$', '*', '?', '<', '>', '`']):
        raise ValueError("Invalid characters detected")

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        result = subprocess.run(['ping', *shlex.split(sanitized_host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}