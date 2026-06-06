from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation with validation
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_route(host: str):
    return {'result': ping(host)}