from fastapi import FastAPI
import subprocess
import shlex
class HostValidator:
    def __init__(self, max_length=255):
        self.max_length = max_length
    def validate(self, host):
        if not host.isalnum() or len(host) > self.max_length:
            raise ValueError('Invalid host')
app = FastAPI()
validator = HostValidator()
@app.get("/ping")
def ping(host: str):
    validator.validate(host)
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}