from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if all(char in allowed_chars for char in host):
        return True
    return False
def safe_ping(host):
    try:
        # Use shlex.split to handle user input safely and ensure the command is properly formatted
        result = subprocess.run(shlex.split(f'ping -c 1 {host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        return safe_ping(host)
    else:
        return {'error': 'Invalid host'}