from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    if host and all(c.isalnum() for c in host) and len(host) <= 255:
        try:
            subprocess.run(['ping', host], check=True, shell=False)
        except subprocess.CalledProcessError as e:
            raise ValueError(f'Ping failed with error: {e}')
    else:
        raise ValueError('Invalid host input')