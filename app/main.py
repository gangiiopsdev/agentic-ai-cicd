from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        args = shlex.split(command)
        return subprocess.run(args, check=True, *args, **kwargs)

app = FastAPI()

def is_safe_host(host):
    # Implement a whitelist of allowed hosts
    return host in ['safehost1', 'safehost2']

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        try:
            SafeSubprocess.run(f'ping {host}')
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        raise ValueError('Host not allowed')

    return {'status': 'completed'}