from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in ('-', '.', '_', ':'))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = shlex.split(f'ping {sanitized_host}')
    subprocess.run(command, check=True, capture_output=True, text=True)
    return {"status": "completed"}