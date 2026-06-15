from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(c if c.isalnum() else '_' for c in input_str)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Use a safe alternative to subprocess.call
    try:
        output = subprocess.check_output(['ping', '-c', '1', sanitized_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}