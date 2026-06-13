from fastapi import FastAPI
import subprocess
import re
import socket

app = FastAPI()

def validate_host(host: str):
    # Regular expression for validating a Hostname/IP
    regex = r'^[a-zA-Z0-9.-]+$'
    if not re.match(regex, host):
        return False
    try:
        socket.gethostbyname(host)
    except socket.gaierror:
        return False
    return True

def safe_ping(host: str):
    # Safe implementation using subprocess.run with shell=False and full path
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'stderr': str(e.stderr.decode())}, 500

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'invalid host'}, 400
    result = safe_ping(host)
    return result