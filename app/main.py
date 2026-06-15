from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        # Ensure the host input is properly sanitized to avoid command injection
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_handler(host: str):
    # Validate the host input to prevent command injection
    if not validate_host_input(host):
        return {'status': 'failed', 'error': 'Invalid host input'}
    return ping(host)

def validate_host_input(input_str: str) -> bool:
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return all(char in allowed_chars for char in input_str)