from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isspace())

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        raise ValueError('Invalid input')
    subprocess.run(['ping', '-c 1'] + shlex.split(f'--{sanitized_host}'), check=True, shell=False)
    return {'status': 'completed'}