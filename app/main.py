from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host input to prevent injection
    if not host.isalnum():
        raise ValueError('Invalid host')
    args = ['ping', host]
    subprocess.call(args, shell=False)

@app.get("/ping")
def ping_route(host: str):
    return {'status': 'completed'}