from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    args = ['ping', host]
    result = subprocess.run(shlex.split(' '.join(args)), capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}