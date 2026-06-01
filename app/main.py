from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command: list[str], **kwargs) -> subprocess.CompletedProcess:
        return subprocess.run(command, check=True, capture_output=True, text=True, **kwargs)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isdigit() and len(host.split('.')) != 4:
        return {'status': 'error', 'message': 'Invalid host format'}
    command = ['ping', '-c', '1', shlex.quote(host)]
    result = SafeSubprocess.run(command)
    return {'status': 'completed', 'output': result.stdout}