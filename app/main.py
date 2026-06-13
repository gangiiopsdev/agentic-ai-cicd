from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    if not host or len(host) > 255:
        raise ValueError('Invalid host parameter')
    return host.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    # Validate the sanitized_host to ensure it's a valid IP or domain name
    if not re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host):
        return {'status': 'error', 'error': 'Invalid host parameter'}
    args = ['ping'] + shlex.split(sanitized_host)
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}