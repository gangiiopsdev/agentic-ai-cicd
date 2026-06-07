from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return shlex.quote(input_string)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}