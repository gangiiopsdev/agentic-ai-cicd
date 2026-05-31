from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    if host.startswith('192.168.') or host.startswith('localhost'):  # Example of safe host validation
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host')