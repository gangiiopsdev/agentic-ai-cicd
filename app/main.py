from fastapi import FastAPI
import subprocess
from shlex import quote

class SafeSubprocess:
    def __init__(self, command: str):
        self.command = command

    def run(self, *args):
        safe_args = [quote(arg) for arg in args]
        subprocess.run([self.command] + list(safe_args), check=True)

global_safe_subprocess = SafeSubprocess('ping')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        global_safe_subprocess.run(host)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}