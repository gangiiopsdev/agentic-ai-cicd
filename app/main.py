from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    safe_host = shlex.quote(host)
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}