from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    if not input_str.strip():
        return None
    if 'ping' in input_str.lower():
        return None
    return input_str
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if sanitized_host is None:
        return {'error': 'Invalid input'}
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.call(args)
    return {'status': 'completed'}