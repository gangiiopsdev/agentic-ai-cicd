from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Implement host validation logic here (e.g., whitelist)
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'invalid host'}
    # Secure implementation
    subprocess.call(['ping', host])
    return {'status': 'completed'}