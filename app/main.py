from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return ''.join(char for char in input_str if char in allowed_chars)

@app.get('/ping')
def ping(host: str):
    sanitized_host = shlex.quote(sanitize_input(host))
    # Secure implementation
    command = ['ping', f'-c 1 {sanitized_host}']
    subprocess.run(command, check=True)
    return {'status': 'completed'}