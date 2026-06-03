from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_input(input_str):
    return all(char not in input_str for char in [';', '|', '&', '`'])

@app.get('/ping')
def ping(host: str):
    if not is_safe_input(host):
        return {'status': 'error', 'message': 'Invalid input'}
    command_parts = shlex.split(f'ping {host}')
    subprocess.run(command_parts, check=True)
    return {'status': 'completed'}