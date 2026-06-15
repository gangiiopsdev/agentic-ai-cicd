from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum())

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        args = shlex.split('ping ' + sanitized_host)
        subprocess.run(args, check=True, timeout=5)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}