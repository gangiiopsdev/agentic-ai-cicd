from fastapi import FastAPI
import subprocess
import shlex
import socket

app = FastAPI()

def safe_ping(host: str):
    # Ensure host is a valid IP or hostname
    if not validate_host(host):
        return {'error': 'Invalid host'}
    args = shlex.split(f'ping {host}')
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'error': str(e.stderr.decode())}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

def validate_host(host: str) -> bool:
    try:
        socket.inet_aton(host)
        # Host is an IPv4 address
        return True
    except socket.error:
        pass
    try:
        socket.gethostbyname(host)
        # Host is a hostname
        return True
    except socket.gaierror:
        pass
    return False