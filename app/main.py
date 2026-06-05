from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in ('.', '-', '_'))

app = FastAPI()

@app.post('/ping')
def ping_host(sanitized_host: str):
    cmd = ['ping', shlex.quote(sanitized_host)]
    output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    return {'status': 'completed', 'output': output.decode()}