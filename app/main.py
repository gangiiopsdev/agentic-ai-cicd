from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Basic sanitization of input
    return ''.join(e for e in input_string if e.isalnum() or e in '._-')

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safe implementation using subprocess.run with shell=False and check=True to raise exception on non-zero exit codes
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}