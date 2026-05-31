from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation with input validation
    if not all(char.isalnum() or char in ['.', '-'] for char in host):
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    subprocess.call(args)

@app.get('/ping')
def ping_route(host: str):
    return ping(host)