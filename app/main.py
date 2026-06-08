from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def is_safe_input(input_str: str) -> bool:
        unsafe_chars = ['&&', ';', '|', '>', '<', '&']
        return not any(char in input_str for char in unsafe_chars)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host or not SafeSubprocess.is_safe_input(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}