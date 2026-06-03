from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in input_string if c in allowed_chars)

app = FastAPI()

@app.get('/ping')
def ping(host: str):    sanitized_host = sanitize_input(host)    try:
        # Validate the sanitized host before using it in the command
        if not all(c.isalnum() or c in '.-' for c in sanitized_host):
            return {'status': 'error', 'error': 'Invalid host'}
        result = subprocess.run(shlex.split(f'ping {sanitized_host}'), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}