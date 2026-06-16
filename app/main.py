from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    return host.isalnum()
def sanitize_input(input_str: str) -> str:
    sanitized = input_str.replace(';', '').replace('&', '')
    return sanitized@app.get('/ping/{host}')def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    sanitized_host = sanitize_input(host)
    # Use subprocess.run with check=True to raise an exception on errors
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}