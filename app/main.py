from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        result = subprocess.run(['ping'] + shlex.split(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}