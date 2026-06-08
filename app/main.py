from fastapi import FastAPI
import subprocess

def check_host(host):
    if not host:
        raise ValueError('Host parameter is required')
    return host

def ping(host: str):
    host = check_host(host)
    command = ['ping', '-c', '1', host]
    result = subprocess.run(command, capture_output=True, text=True, check=False, shell=False, cwd='/safe/path')
    return {'status': 'completed', 'output': result.stdout}