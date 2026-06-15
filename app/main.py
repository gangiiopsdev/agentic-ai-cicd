from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    command = ['ping', '-c', '1'] + [shlex.quote(arg) for arg in host.split()]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e.stderr}')
def is_valid_host(host: str) -> bool:
    return all(c.isalnum() or c in ['-', '.'] for c in host)