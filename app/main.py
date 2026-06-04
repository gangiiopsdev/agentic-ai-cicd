from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(host: str) -> str:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        command = shlex.split('ping ' + sanitized_host)
        result = subprocess.run(command, capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}