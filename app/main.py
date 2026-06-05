from fastapi import FastAPI
import subprocess
import re
def ping(host: str):
    # Regular expression to validate IP address and domain name
    pattern = r'^([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|[a-zA-Z0-9-.]+)$'
    if re.match(pattern, host):
        allowed_hosts = ['example.com', '192.168.0.1']  # Add more allowed hosts as needed
        if host in allowed_hosts:
            try:
                result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
            except subprocess.CalledProcessError as e:
                return {'status': 'failed', 'error': str(e)}
        else:
            return {'status': 'failed', 'error': 'Host not allowed'}
    else:
        return {'status': 'failed', 'error': 'Invalid host format'}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)