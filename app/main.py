from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        cmd = ['ping', '-c', '1'] + [shlex.quote(arg) for arg in host.split()]
        subprocess.run(cmd, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}