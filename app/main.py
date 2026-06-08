from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in ['.', '-', '_'])

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', shlex.quote(sanitized_host)]  # Use shlex.quote to escape the host parameter
    result = subprocess.run(args, capture_output=True, text=True, check=True, shell=False)  # Set shell=False explicitly
    return {'status': 'completed', 'output': result.stdout}