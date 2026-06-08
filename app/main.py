from fastapi import FastAPI
import subprocess
import shlex
import os

def safe_host(host):
    # Validate and sanitize the host input to prevent command injection
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    if host in allowed_hosts:
        return True
    return False

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if safe_host(host):
        # Secure implementation with absolute path and argument handling
        result = subprocess.run(['/usr/bin/ping', '-c 1'] + shlex.split(shlex.quote(host)), capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}

# Enhanced security measures
import re

def validate_host(host):
    # Regex to match valid hostnames and IP addresses
    pattern = r'^[a-zA-Z0-9.-]+$'
    if re.match(pattern, host) and safe_host(host):
        return True
    return False

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        result = subprocess.run(['/usr/bin/ping', '-c 1'] + shlex.split(shlex.quote(host)), capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}