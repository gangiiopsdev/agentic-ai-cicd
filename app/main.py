from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join([char for char in input_str if char in allowed_chars])

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent shell injection
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping {sanitized_host}')
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}