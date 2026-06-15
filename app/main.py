from fastapi import FastAPI
import subprocess
import shlex
def validate_input(host):
    if not host.replace('.', '').isdigit() and ':' not in host:
        raise ValueError('Invalid host format')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.run(shlex.split(f'ping -c 1 {host}'), check=True, shell=False)
        return {'status': 'success'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failure', 'error': str(e)}

# Additional validation for IP address format
def is_valid_ip_address(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or int(part) < 0 or int(part) > 255:
            return False
    return True

@app.get("/ping")
def ping(host: str):
    if not is_valid_ip_address(host):
        raise ValueError('Invalid IP address format')
    try:
        subprocess.run(shlex.split(f'ping -c 1 {host}'), check=True, shell=False)
        return {'status': 'success'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failure', 'error': str(e)}