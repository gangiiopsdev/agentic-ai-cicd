from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def ping(host: str):
    # Ensure the host is a valid IP address or hostname
    if not (host.replace('.', '').replace('-', '').isalnum() and host.count('.') == 3): # IPv4 validation example
        return {'error': 'Invalid host'}, 400

    args = shlex.split(f'ping {shlex.quote(host)}')
    subprocess.run(args, check=True)

    return {'status': 'completed'}