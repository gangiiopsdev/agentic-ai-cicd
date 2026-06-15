from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host: str) -> bool:
    return host.isalnum()

def sanitize_input(input_str: str) -> str:
    sanitized = input_str.replace(';', '').replace('&', '')
    return sanitized

@app.get('/ping/{host}')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    sanitized_host = sanitize_input(host)
    args = shlex.split('ping ' + sanitized_host)
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}