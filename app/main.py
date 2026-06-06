from fastapi import FastAPI
import shlex
import subprocess
import re
class SafePing:
    allowed_hosts = ['example.com', 'test.com']  # Define a whitelist of allowed hosts

    def __init__(self):
        pass

    def safe_ping(self, host):
        if not re.match(r'^[a-zA-Z0-9.-]+$', host) or host not in self.allowed_hosts:
            return {'status': 'error', 'message': 'Host is not allowed'}
        try:
            args = shlex.split('ping {}'.format(shlex.quote(host)))
            result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'stderr': e.stderr.decode()}

app = FastAPI()
ping_service = SafePing()

@app.get("/ping")
def ping(host: str):
    return ping_service.safe_ping(host)