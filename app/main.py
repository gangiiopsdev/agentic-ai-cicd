from fastapi import FastAPI
import subprocess
from typing import List

app = FastAPI()

def sanitize_input(input_str: str) -> str:
    return ''.join(c for c in input_str if c.isalnum() or c in ['.', '-'])

@app.get('/ping/{host}')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}