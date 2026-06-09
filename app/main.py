from fastapi import FastAPI
import subprocess
def ping_host(host):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout