from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        command = ['ping'] + shlex.split(host)
        output = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}