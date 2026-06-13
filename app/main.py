from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return bool(re.match(f'^[{allowed_chars}]*$', host))

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        result = subprocess.run(shlex.split(f'ping {shlex.quote(host)}'), capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid host input'}