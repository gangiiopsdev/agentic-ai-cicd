from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Unsafe host provided')
    args = shlex.split(f'ping {host}')
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed'}

def is_safe_host(host: str) -> bool:
    # Implement logic to check if the host is safe
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts