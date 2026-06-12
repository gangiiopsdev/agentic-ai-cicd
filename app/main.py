from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', quote(host)])

@app.get("/ping")
def ping_route(host: str):
    return {'result': ping(host)}