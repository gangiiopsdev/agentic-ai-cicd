from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.safe_hosts = ['example.com', 'localhost']

    def is_safe_hostname(self, hostname):
        return hostname in self.safe_hosts

app = FastAPI()
safe_ping = SafePing()

@app.get("/ping")
def ping(host: str):
    if not safe_ping.is_safe_hostname(host):
        raise ValueError('Invalid host name')
    args = shlex.split(f'ping {host}')
    try:
        result = subprocess.run(args, check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'stdout': e.stdout.decode(), 'stderr': e.stderr.decode()}
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}