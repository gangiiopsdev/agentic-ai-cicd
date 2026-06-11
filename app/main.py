from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more allowed hosts as needed
    return host in allowed_hosts

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in '.-:=')

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Host is not allowed')
    sanitized_host = sanitize_input(host)
    command = ['ping', shlex.quote(sanitized_host)]
    subprocess.run(command, check=True)
    return {'status': 'completed'}