from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    if not host:
        return {'status': 'failed', 'output': 'Host parameter is empty'}
    try:
        result = subprocess.run(['ping'] + shlex.split('-c 1 ' + host), capture_output=True, text=True, check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'output': str(e)}
    return {'status': 'completed', 'output': result.stdout}