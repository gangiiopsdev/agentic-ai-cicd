from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isnumeric() or int(host) < 1 or int(host) > 254:
        raise ValueError('Invalid host')
    # Sanitize input by using a safe range of hosts
    safe_hosts = ['192.168.1.' + str(i) for i in range(1, 255)]
    if host not in safe_hosts:
        raise ValueError('Host is out of allowed range')
    subprocess.run(['ping', '-c', '1', host], check=True)
    return {'status': 'completed'}