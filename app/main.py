from fastapi import FastAPI
import subprocess
import shlex
from shlex import quote as cmd_quote

class SafeSubprocess:
    @staticmethod
def safe_run(command: str):
        args = shlex.split(command)
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    command = f'ping {cmd_quote(host)}'
    try:
        result = SafeSubprocess.safe_run(command)
        return result
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}