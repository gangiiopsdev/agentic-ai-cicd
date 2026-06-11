from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host: str) -> str:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.~'
    return ''.join(char for char in host if char in allowed_chars)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_host(host)
    args = ['ping', shlex.quote(escaped_host)]  # Use shlex.quote to safely include user input
    try:
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}