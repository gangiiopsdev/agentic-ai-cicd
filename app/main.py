from fastapi import FastAPI
import subprocess
def ping_host(host):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)