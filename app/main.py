from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Basic input sanitization (more robust methods are recommended)
    return ''.join(filter(str.isalnum, input_string))

@app.get('/ping')
def ping(host: str):  # Sanitize the input to prevent injection attacks
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}