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
        return {'status': 'error', 'message': 'Invalid input'}
    result = subprocess.run(['ping'] + shlex.split(sanitized_host), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}