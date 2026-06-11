from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host: str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    if not all(char in allowed_chars for char in host):
        raise ValueError('Invalid characters in host name')

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    args = ['ping', shlex.quote(host)]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        return {'status': 'failed', 'error': error.decode('utf-8')}
    else:
        return {'status': 'completed', 'output': output.decode('utf-8')}