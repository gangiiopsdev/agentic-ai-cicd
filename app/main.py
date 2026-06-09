from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        command = ['ping'] + shlex.split(host)
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}