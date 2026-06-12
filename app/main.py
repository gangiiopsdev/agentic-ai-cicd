from fastapi import FastAPI
import subprocess
class Pinger:
    def __init__(self):
        self.allowed_hosts = {'localhost', '127.0.0.1'}

    async def ping(self, host: str) -> dict:
        if host.strip() not in self.allowed_hosts:
            return {'status': 'unauthorized'}
        try:
            result = await subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}