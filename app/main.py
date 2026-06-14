from fastapi import FastAPI
import re
import ipaddress
from typing import Dict

app = FastAPI()

async def ping(host: str) -> Dict[str, str]:
    try:
        # Validate host to ensure it's a safe hostname or IP address
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return {'status': 'error', 'message': 'Invalid host'}
        # Use a whitelist of allowed hosts
        allowed_hosts = ['8.8.8.8', '1.1.1.1']  # Example list
        if host not in allowed_hosts:
            return {'status': 'error', 'message': 'Host is not allowed'}
        result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.get('/ping')
def ping_host(host: str) -> Dict[str, str]:
    return ping(host)