from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum():
        raise ValueError('Invalid input for host')
    args = ['ping', '-c', '1', host]
    subprocess.run(args, check=True, timeout=5)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)