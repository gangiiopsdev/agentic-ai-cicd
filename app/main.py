from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Ensure host is a valid IP address before executing the command
    if not validate_ip_address(host):
        return {'status': 'failed', 'error': 'Invalid IP address'}
    try:
        subprocess.run(['/bin/ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.stderr.decode())}
def validate_ip_address(ip):\n    import socket\n    try:\n        socket.inet_pton(socket.AF_INET, ip)\n    except socket.error:\n        return False\n    return True