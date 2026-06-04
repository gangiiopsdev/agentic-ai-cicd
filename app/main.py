from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Implement a whitelist of allowed hosts
    safe_hosts = ['example.com', 'another-example.com']
    return host in safe_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}