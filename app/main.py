from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation
    if host.isalnum():
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid hostname')