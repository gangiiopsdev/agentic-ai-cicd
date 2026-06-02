from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return input_string.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or '..' in host:
        raise ValueError('Invalid host input')
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}