from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        import shlex
        command = shlex.split(command)
        return subprocess.run(command, check=True, *args, **kwargs)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        raise ValueError('Invalid host name')
    SafeSubprocess.run(f'ping --no-host-alias --non-privileged {host}', check=True)
    return {'status': 'completed'}