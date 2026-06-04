from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    # Basic sanitization example: remove any non-alphanumeric characters and whitespace
    return ''.join(c for c in input_string if c.isalnum())

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}