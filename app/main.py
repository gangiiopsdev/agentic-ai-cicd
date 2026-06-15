from fastapi import FastAPI
import subprocess
ALLOWED_HOSTS = ['example.com']

app = FastAPI()

def ping(host: str):
    if host in ALLOWED_HOSTS:
        # Use a whitelist of allowed hosts and avoid using subprocess for ping
        return {'status': 'Host not supported'}
    else:
        raise ValueError('Unauthorized host')
    return {'status': 'completed'}