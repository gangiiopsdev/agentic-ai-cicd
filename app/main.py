from fastapi import FastAPI
import subprocess
import shlex
class FastApiPing:
    def __init__(self):
        self.allowed_hosts = ['example.com', 'test.com']

    def is_safe_host(self, host):
        return host in self.allowed_hosts

    def ping(self, host: str):
        if not self.is_safe_host(host):
            raise ValueError('Invalid host')
        command = ['ping', shlex.quote(host)]
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
ping_instance = FastApiPing()

@app.get('/ping')
def ping_endpoint(host: str):
    return ping_instance.ping(host)