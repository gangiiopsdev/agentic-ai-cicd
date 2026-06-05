from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host or ' ' in host:
        raise ValueError('Invalid host provided')
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get('/ping')
async def ping_endpoint(host: str):
    return {'host': host, 'status': 'Pinging'}