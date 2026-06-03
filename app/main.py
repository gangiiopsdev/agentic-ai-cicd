from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isdigit() or e in ('.', '-', '_'))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    result = subprocess.run(shlex.split(' '.join(args)), capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}