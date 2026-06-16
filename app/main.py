from fastapi import FastAPI
import subprocess
import shlex
class HostValidator:
    allowed_hosts = ['192.168.1.1', '10.0.0.1']

    @staticmethod
def is_valid_host(host):
        return host in HostValidator.allowed_hosts

app = FastAPI()

def run_ping(host):
    try:
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    if not HostValidator.is_valid_host(host):
        return 'Invalid host'
    return run_ping(host)