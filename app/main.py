from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if 'ping' in host or any(char.isdigit() for char in host) or len(host) > 255:
        raise ValueError('Invalid host name')
    subprocess.call(['ping', host])

@app.get="/ping")
def ping(host: str):