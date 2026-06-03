from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with full path and validation
    if host.strip() == 'localhost' or host.startswith('127.0.0.1'):
        subprocess.run(['/bin/ping', host], check=True)
    else:
        raise ValueError('Invalid host for ping operation')

@app.get("/ping")
def get_ping(host: str):
    return ping(host)