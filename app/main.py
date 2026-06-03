from fastapi import FastAPI
import subprocess
import shlex
from sanic.response import json

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', '-c', '1', shlex.quote(sanitized_host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return json({'status': 'completed', 'output': result.stdout})
    except subprocess.CalledProcessError as e:
        return json({'status': 'error', 'message': str(e)}, status=500)