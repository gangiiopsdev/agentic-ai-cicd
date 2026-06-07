from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation with input validation
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        return {'status': 'invalid_host'}
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}

@app.get("/ping")
def ping_route(host: str): return ping(host)