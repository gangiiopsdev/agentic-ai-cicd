from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}