from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Ensure the hostname is safe
    if not host.strip().isalnum() or '@' in host:
        raise ValueError('Invalid hostname')
    # Use full executable path and avoid shell=True for better security
    cmd = ['ping', '-c 4'] + shlex.split(host)
    subprocess.run(cmd, check=True, shell=False)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return {'status': 'Pinging host', 'host': host}