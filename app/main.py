from fastapi import FastAPI
import re
import subprocess
import ipaddress

app = FastAPI()

def ping(host: str):
    try:
        # Validate host to ensure it's a safe hostname or IP address
        if not re.match(r'^[a-zA-Z0-9.-]+$', host) or not (ipaddress.ip_address(host) if '.' in host else ipaddress.ip_network(host)):
            return {'status': 'error', 'message': 'Invalid host'}
        result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.get('/ping')
def ping_host(host: str):
    return ping(host)