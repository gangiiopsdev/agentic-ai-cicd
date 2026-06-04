from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        args = shlex.split(f'ping -c 4 {host}')  # Limit the number of pings to avoid potential denial-of-service attacks
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}