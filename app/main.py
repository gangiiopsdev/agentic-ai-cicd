from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    if not isinstance(input_string, str) or '&&' in input_string or ';' in input_string:
        raise ValueError('Invalid input')
    return input_string

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        args = shlex.split(f'ping {sanitized_host}')
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}