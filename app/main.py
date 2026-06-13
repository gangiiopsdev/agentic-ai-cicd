from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ['.', '-', '_'])

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        args = shlex.split(f'ping {sanitized_host}')
        subprocess.call(args, shell=False)
    except Exception as e:
        return {'error': str(e)}
    return {'status': 'completed'}