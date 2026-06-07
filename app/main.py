from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def safe_check_output(command: str, *args, **kwargs):
        if 'shell' in kwargs and kwargs['shell']:
            raise ValueError('Shell execution is not allowed')
        return subprocess.check_output(shlex.split(command), *args, **kwargs)

app = FastAPI()

def ping(host: str):
    try:
        output = SafeSubprocess.safe_check_output(f'ping {shlex.quote(host)}', stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate and sanitize host input to prevent injection attacks
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return ping(host)