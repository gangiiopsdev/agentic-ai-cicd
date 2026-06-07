from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_input(host: str) -> bool:
    unsafe_chars = ['&&', ';', '|', '>', '<', '&']
    return not any(char in host for char in unsafe_chars)

@app.get('/ping')
def ping(host: str):
    if not host or not is_safe_input(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}