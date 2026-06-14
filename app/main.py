from fastapi import FastAPI, HTTPException
import subprocess
import shlex

global ALLOWED_HOSTS = {'example.com', 'localhost'}

app = FastAPI()

def sanitize_input(user_input):
    return shlex.quote(user_input)

def validate_host(host):
    if host not in ALLOWED_HOSTS:
        raise HTTPException(status_code=400, detail='Invalid host')
    return host

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(validate_host(host))
    command = ['ping', '-c 1', sanitized_host]  # Limiting the number of pings to 1 for security
    process = subprocess.Popen(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {'status': 'completed', 'output': output.decode(), 'error': error.decode() if error else None}