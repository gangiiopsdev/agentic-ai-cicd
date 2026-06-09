from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_safe_input(input_str):
    return re.match(r'^[a-zA-Z0-9.-]+$', input_str) is not None

@app.post('/ping/')
def ping(host: str):
    if not is_safe_input(host):
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}