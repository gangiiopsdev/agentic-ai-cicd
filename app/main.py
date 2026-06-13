from fastapi import FastAPI
import subprocess
class PingApp:
    def __init__(self):
        self.app = FastAPI()

    def ping(self, host: str):
        try:
            output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, shell=False)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}

    @app.get("/ping")
    def ping_endpoint(self, host: str):
        if not self.is_valid_host(host):
            return {'status': 'failed', 'error': 'Invalid host'}
        return self.ping(host)

    def is_valid_host(self, host: str) -> bool:
        import re
        pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
        return bool(pattern.match(host))