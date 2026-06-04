from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host):
    # Implement validation logic here, e.g., allow only certain hostnames/IPs
    allowed_hosts = ['example.com', '192.168.1.1']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        # Use regex to ensure the host is a valid hostname/IP
        if re.match(r'^[a-zA-Z0-9.-]+$', host) and len(host.split('.')) == 4:
            args = ['ping', '-c', '1', host]  # Limit the number of pings to avoid potential DoS
            subprocess.run(args, check=True)
            return {"status": "completed"}
        else:
            return {"error": "Invalid host format"}
    else:
        return {"error": "Invalid host"}