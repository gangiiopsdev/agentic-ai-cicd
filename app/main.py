from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only alphanumeric characters and hyphens
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-'
    return all(char in allowed_chars for char in host)

def sanitize_input(input_str: str) -> str:
    # Sanitize input to prevent command injection
    return shlex.quote(input_str)

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host input')
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}