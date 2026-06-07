from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', '192.168.1.1']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        args = ['ping', '-c', '1']  # Limit the number of pings to avoid potential DoS
        result = subprocess.run(args + [host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'error': 'Invalid host'}