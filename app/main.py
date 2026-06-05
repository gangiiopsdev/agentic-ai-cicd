from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if host in allowed_hosts:
        return host
    else:
        raise ValueError('Host not allowed')

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    command = ['ping', shlex.quote(sanitized_host)]
    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}