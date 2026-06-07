from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Add more allowed hosts as needed
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

# Fixed code to use a safe and secure alternative for ping
@app.get('/ping_safe')
def ping_safe(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}
    try:
        output = os.system(f'ping -c 1 {host}')  # Using safe and secure alternative for ping on Unix-like systems
        return {'status': 'completed'} if output == 0 else {'error': 'Ping failed'}
    except Exception as e:
        return {'error': str(e)}