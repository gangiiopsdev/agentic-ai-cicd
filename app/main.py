from fastapi import FastAPI
import subprocess
import shlex
from html import escape

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e.isdigit() or e.isspace())

@app.get('/ping')
def ping(host: str):
    sanitized_host = escape(host)
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.run(args, check=True)

    return {'status': 'completed'}