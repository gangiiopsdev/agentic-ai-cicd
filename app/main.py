from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        # Using check_output instead of call for better error handling and no shell=True
        cmd = ['ping', host]
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}