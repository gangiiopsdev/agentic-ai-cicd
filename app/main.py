from fastapi import FastAPI
import subprocess
import shlex
def safe_run(command):
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return result.stdout

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isdigit() or e in ('.', '-', '_'))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', sanitized_host]
    output = safe_run(command)
    return {'status': 'completed', 'output': output}