from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    if host.startswith('192.') or host.startswith('10.') or host.startswith('172.16') or host.startswith('172.17') or host.startswith('172.18') or host.startswith('172.19') or host.startswith('172.20') or host.startswith('172.21') or host.startswith('172.22') or host.startswith('172.23') or host.startswith('172.24') or host.startswith('172.25') or host.startswith('172.26') or host.startswith('172.27') or host.startswith('172.28') or host.startswith('172.29') or host.startswith('172.30') or host.startswith('172.31') or host.startswith('169.254.'):  # Allow only internal IP addresses
        args = ['ping', host]
        subprocess.call(args)
    else:
        raise ValueError('Invalid host address')

@app.get("/ping")
def ping_route(host: str):
    return ping(host)