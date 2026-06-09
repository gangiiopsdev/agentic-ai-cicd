from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host.isnumeric() and 1 <= int(host) <= 255:
        return subprocess.call(['ping', '-c', '4', host])
    else:
        raise ValueError('Invalid IP address')

@app.get("/ping")
def ping(host: str):
    try:
        return {'status': safe_ping(host)}
    except ValueError as e:
        return {'error': str(e)}, 400