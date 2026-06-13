from fastapi import FastAPI
import subprocess
import shlex
import re

class CommandSanitizer:
    @staticmethod
    def sanitize(input_string):
        pattern = r'^[a-zA-Z0-9.-]+$'
        return re.match(pattern, input_string) is not None

app = FastAPI()

async def ping(host: str):
    if not CommandSanitizer.sanitize(host):
        raise ValueError('Invalid host')
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}