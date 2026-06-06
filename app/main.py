from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isdigit() or e in ('.', '-', '_'))

def execute_ping(sanitized_host):
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if sanitized_host and len(sanitized_host) <= 255:
        execute_ping(sanitized_host)
    return {"status": "completed"}