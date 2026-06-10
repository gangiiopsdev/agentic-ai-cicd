from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_str if char in allowed_chars)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping {shlex.quote(sanitized_host)}')
    subprocess.run(args, check=True, text=True, capture_output=True)
    return {'status': 'completed', 'output': args[1]}