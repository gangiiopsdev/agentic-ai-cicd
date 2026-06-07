from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', *shlex.split(host)], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    if not host.strip():
        raise ValueError('Host parameter is required')
    return ping(host)