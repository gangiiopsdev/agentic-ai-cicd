from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_host(host):
    return shlex.quote(host)

def validate_interface(interface):
    allowed_interfaces = ['eth0', 'wlan0']  # Add more interfaces as needed
    if interface in allowed_interfaces:
        return interface
    else:
        return 'eth0'

@app.get('/ping')
def ping(host: str, interface: str = None):
    sanitized_host = sanitize_host(host)
    interface = validate_interface(interface or os.getenv('PRIMARY_INTERFACE', 'eth0'))
    try:
        output = subprocess.run(['ping', '-c', '1', f'-I {interface} {sanitized_host}'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}