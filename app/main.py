from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate host to ensure it's a valid IP address or hostname
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}

    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)

def is_valid_host(host: str) -> bool:
    import socket
    try:
        socket.inet_aton(host)
        return True  # It's a valid IP address
    except socket.error:
        pass
    try:
        socket.gethostbyname(host)
        return True  # It's a valid hostname
    except socket.gaierror:
        return False  # Invalid host