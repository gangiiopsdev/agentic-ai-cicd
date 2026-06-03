from fastapi import FastAPI
import subprocess
from typing import List
import shlex

class PingService:
    @staticmethod
def ping(host: str):
        if not host.strip():
            raise ValueError('Invalid host provided')
        args = ['ping', '-c', '1'] + shlex.split(host)
        result = subprocess.run(args, capture_output=True, text=True, check=False)
        return {'status': 'completed' if result.returncode == 0 else 'failed', 'output': result.stdout}

app = FastAPI()

def ping_route(host: str):
    return PingService.ping(host)