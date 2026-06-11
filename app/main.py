from fastapi import FastAPI
import subprocess
import shlex
from subprocess import Popen, PIPE

class FastAPISubprocess:
    @staticmethod
def ping(host: str):
        sanitized_host = ''.join(e for e in host if e.isalnum() or e in ('.', '-', '_', ':'))
        if 'ping' not in sanitized_host:
            return {'error': 'Invalid host input'}
        try:
            result = Popen(['ping', sanitized_host], stdout=PIPE, stderr=PIPE)
            output, error = result.communicate()
            return {'status': 'completed', 'output': output.decode('utf-8'), 'error': error.decode('utf-8')}
        except Exception as e:
            return {'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return FastAPISubprocess.ping(host)