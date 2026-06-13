from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

app = FastAPI()

@app.get('/ping')
def ping(host: str = '8.8.8.8'):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    return {'status': 'completed', 'output': output.decode()}