from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def call(command: str, **kwargs):
        args = shlex.split(command)
        return subprocess.run(args, check=True, **kwargs)

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        SafeSubprocess.call(f'ping {host}')
    else:
        raise ValueError('Unauthorized host')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}