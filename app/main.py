from fastapi import FastAPI
import subprocess
import shlex
from shlex import quote

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isspace())

@app.get("/ping")
def ping(host: str):
    # Secure implementation with sanitized and quoted input
    sanitized_host = quote(sanitize_input(host))
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}