from fastapi import FastAPI
import subprocess
import re
import shlex

class PingService:
    def __init__(self):
        self.valid_hostnames = ['example.com', 'localhost']  # Define a whitelist of valid hostnames

    def is_valid_hostname(self, hostname):
        return hostname in self.valid_hostnames

app = FastAPI()
ping_service = PingService()

def ping(host: str):
    if not ping_service.is_valid_hostname(host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        cmd = ['ping', '-c', '1', shlex.quote(host)]
        output = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}