from fastapi import FastAPI
import subprocess
from typing import Optional
import shlex

class SafeSubprocess:
    @staticmethod
def run(command: str, **kwargs) -> bytes:
        try:
            return subprocess.check_output(shlex.split(command), stderr=subprocess.STDOUT, **kwargs)
        except subprocess.CalledProcessError as e:
            return e.output

app = FastAPI()

@app.get("/ping")
def ping(host: Optional[str] = None) -> dict:
    if host is None or not isinstance(host, str) or len(host.strip()) == 0:
        return {'error': 'Invalid input'}
    command = f'ping {host}'
    output = SafeSubprocess.run(command)
    return {'status': 'completed', 'output': output.decode('utf-8')}