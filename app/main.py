from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ['-', '_', '.', '@'])

def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.stderr}