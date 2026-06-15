from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def call(command: str, *args, **kwargs):
        args = shlex.split(command)
        return subprocess.run(args, check=True, capture_output=True, text=True)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    command = f'ping {shlex.quote(host)}'
    try:
        result = SafeSubprocess.call(command)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}