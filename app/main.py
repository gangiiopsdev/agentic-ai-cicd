from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in ['-', '.', '_', '@'])

cmd = ['ping', '-c', '1', sanitize_input(host)]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}