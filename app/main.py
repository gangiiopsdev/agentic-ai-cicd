from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args, check=True)

def secure_ping(host: str):
    if not isinstance(host, str) or len(host.strip()) == 0:
        raise ValueError('Invalid host name')
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return secure_ping(host)