from fastapi import FastAPI
import subprocess
import shlex
cimport = ['ping']

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(char for char in input_str if char.isalnum() or char == '.')[:64]

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {'error': 'Invalid host'}, 400
    subprocess.run(shlex.split(f'{cimport[0]} {sanitized_host}'), check=True, capture_output=True)
    return {'status': 'completed'}