from fastapi import FastAPI
import subprocess
import shlex

class SanitizedPing:
    def __init__(self):
        self.allowed_hosts = ['google.com', 'example.com']

    def is_host_allowed(self, host: str) -> bool:
        return host in self.allowed_hosts

app = FastAPI()
sanitized_ping = SanitizedPing()

@app.get('/ping')
def ping(host: str):
    if sanitized_ping.is_host_allowed(host):
        command = ['ping', shlex.quote(host)]
        subprocess.call(command)
    return {'status': 'completed'}