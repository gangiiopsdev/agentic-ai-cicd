from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(char for char in input_string if char.isalnum() or char in ['.', '-'])

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        subprocess.run(shlex.split(f'ping {sanitized_host}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': subprocess.PIPE.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}