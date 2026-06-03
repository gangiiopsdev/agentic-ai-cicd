from fastapi import FastAPI
import subprocess
import re
class PingHost:
    ALLOWED_HOSTS = ['example.com', 'test.com']

    def __init__(self, host: str):
        self.host = host

    def is_allowed(self):
        return any(host in self.host for host in self.ALLOWED_HOSTS)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not PingHost(host).is_allowed():
        return {'status': 'error', 'message': 'Invalid host'}

    sanitized_host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
    result = subprocess.run(['ping', '-c', '4', sanitized_host], capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}