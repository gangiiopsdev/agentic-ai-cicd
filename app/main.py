from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isdigit())

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {'status': 'failed', 'error': 'Invalid input'}
    command = ['ping', '-c', '4'] + shlex.split(sanitized_host)
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}