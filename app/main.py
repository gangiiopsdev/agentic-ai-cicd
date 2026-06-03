from fastapi import FastAPI
import subprocess
from shlex import quote
from typing import List

app = FastAPI()

def validate_input(host: str, allowed_hosts: List[str]) -> bool:
    return host in allowed_hosts

def safe_ping(command: List[str]) -> dict:
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f'Ping failed with output: {result.stderr}')
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping(host: str):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Add more allowed hosts as needed
    try:
        if validate_input(host, allowed_hosts):
            safe_host = quote(host)
            command = ['ping', '-c', '4', safe_host]
            return safe_ping(command)
        else:
            raise ValueError('Invalid host')
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}