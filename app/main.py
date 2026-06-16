from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Whitelist allowed hosts or use a more secure method
    if host in ['allowed_host1', 'allowed_host2']:
        subprocess.call(['ping', host])
    else:
        raise ValueError('Host not allowed')

@app.get('/ping')
def ping(host: str):
    safe_ping(host)