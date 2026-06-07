from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c == '.')

@app.get('/ping')
def ping(host: str):
    # Sanitize input to avoid injection vulnerabilities
    host = sanitize_input(host)
    if not host:
        raise ValueError('Invalid host name')
    subprocess.run(['ping', shlex.quote(host)], check=True, shell=False)
    return {'status': 'completed'}