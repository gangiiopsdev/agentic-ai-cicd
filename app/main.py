from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.app = FastAPI()

    async def ping(self, host: str):
        if not host.isalnum():
            raise ValueError('Invalid input')
        try:
            output = subprocess.check_output(shlex.split(f'ping {host}'), shell=False, stderr=subprocess.STDOUT)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}