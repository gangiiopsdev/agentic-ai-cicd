from fastapi import FastAPI
import subprocess
from shlex import quote
def ping(host: str):
    args = ['ping', quote(host)]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}