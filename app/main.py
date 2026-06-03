from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_input(input_string):
    # Basic sanitization of input
    return ''.join(e for e in input_string if e.isalnum() or e in '._-')

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Use a more secure approach to execute the command
    try:
        result = subprocess.run(['ping', '-c', '1'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'output': str(e)}