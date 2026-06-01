from fastapi import FastAPI
import subprocess
from subprocess import Popen, PIPE, DEVNULL
import shlex

def ping(host: str):
    try:
        command = ['ping'] + shlex.split(host)
        process = Popen(command, stdout=DEVNULL, stderr=PIPE)
        output, error = process.communicate()
        if process.returncode == 0:
            return {'status': 'completed'}
        else:
            return {'error': str(error.decode('utf-8'))}
    except Exception as e:
        return {'error': str(e)}