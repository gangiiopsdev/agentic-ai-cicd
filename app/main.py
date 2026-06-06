from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command: str, **kwargs):
        args = shlex.split(command)
        return subprocess.run(args, **kwargs)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    command = f'ping -c 1 {host}'
    result = SafeSubprocess.run(command)
    return {'status': 'completed', 'result': result.returncode}