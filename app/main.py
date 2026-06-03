from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    args = ['ping', host]
    if '/' in host or '\' in host:
        raise ValueError('Unsafe host provided')
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)