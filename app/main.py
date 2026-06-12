from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        cmd = ['ping', host]
        args = shlex.split(' '.join(cmd))
        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}