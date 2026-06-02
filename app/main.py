from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def escape_input(user_input):
    return quote(user_input)

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']  # Define a whitelist of allowed hosts
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        escaped_host = escape_input(host)
        result = subprocess.run(['ping', '-c', '1', escaped_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid host'}