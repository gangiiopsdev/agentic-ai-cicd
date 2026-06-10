from fastapi import FastAPI
import subprocess
import shlex

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char for char in host if char in allowed_chars)

def validate_host(host):
    # Define a set of allowed hosts or patterns
    allowed_hosts = {'example.com', 'test.example.com'}
    if host in allowed_hosts:
        return True
    return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        sanitized_host = sanitize_host(host)
        args = ['ping', shlex.quote(sanitized_host)]
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}