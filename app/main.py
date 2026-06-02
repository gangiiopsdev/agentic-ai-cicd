from fastapi import FastAPI
import subprocess
import shlex

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ['-', '.', '_', '/', ':'])

def execute_ping(host):
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)