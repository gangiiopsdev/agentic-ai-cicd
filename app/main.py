from fastapi import FastAPI
import os
from sanic.response import json

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = os.system(f'ping {sanitized_host}')
        return json({'status': 'completed', 'output': ''})
    except Exception as e:
        return json({'status': 'error', 'message': str(e)}, status=500)