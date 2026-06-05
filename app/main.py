from fastapi import FastAPI
import subprocess
import shlex
import os
from typing import List

current_user = os.getlogin()
app = FastAPI()

def validate_host(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

def ping(host: str):
    if not validate_host(host):
        raise ValueError('Host is not allowed')

    args = shlex.split(f'ping {host}')
    subprocess.run(['sudo', '-u', current_user, 'sh', '-c', *args], check=True)
    return {'status': 'completed'}