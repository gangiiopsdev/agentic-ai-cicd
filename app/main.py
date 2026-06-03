from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def _ping(host: str) -> str:
    # Secure implementation using shlex for proper argument handling
    args = ['ping'] + shlex.split(host)
    try:
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e)

def _is_valid_host(host: str) -> bool:
    # Implement validation logic for the host input here
    # For example, check if it is a valid IP address or hostname
    import socket
    try:
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False

def ping(host: str):
    if _is_valid_host(host):
        output = _ping(host)
        return {'status': 'completed', 'output': output}
    else:
        return {'status': 'error', 'error': 'Invalid host'}