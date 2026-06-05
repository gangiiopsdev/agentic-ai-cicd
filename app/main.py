from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Implement logic to check if the host is safe (e.g., whitelist specific hosts)
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr.decode()}