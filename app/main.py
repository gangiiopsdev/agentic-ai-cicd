from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['example.com', 'test.local']  # Define allowed hosts here

    def sanitize_host(self, host):
        return ''.join(c if c.isalnum() or c in '-.' else '_' for c in host)

    def is_safe_host(self, host):
        return host in self.allowed_hosts

app = FastAPI()
safe_ping = SafePing()

@app.get('/ping')
def ping(host: str):
    if not safe_ping.is_safe_host(safe_ping.sanitize_host(host)):
        return {'status': 'error', 'message': 'Invalid host'}
    args = shlex.split(f'ping -c 1 {shlex.quote(safe_ping.sanitize_host(host))}')
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}