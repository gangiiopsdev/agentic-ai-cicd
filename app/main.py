from fastapi import FastAPI
import socket
import re
import subprocess

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

def safe_ping_command(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    return ['ping', '-c', '1', host]

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        command = safe_ping_command(host)
        subprocess.run(command, check=True, shell=False)  # Fixed here by adding shell=False
        return {'status': 'completed'}
    except ValueError as e:
        return {'status': 'invalid host', 'error': str(e)}, 400
    except subprocess.CalledProcessError as e:
        return {'status': 'ping failed', 'error': str(e)}, 500