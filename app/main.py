from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host: str) -> bool:
    # Define a list of allowed characters or patterns
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    for char in host:
        if char not in allowed_chars:
            return False
    return True

def sanitize_host(host: str) -> str:
    # Sanitize input by removing disallowed characters
    return ''.join(char for char in host if char.isalnum() or char in '-.')

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize host input
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        output = subprocess.run(['ping'] + shlex.split(sanitize_host(host)), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}