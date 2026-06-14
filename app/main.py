from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    # Implement host validation logic here, e.g., allow only specific hosts.
    return host in ['host1', 'host2']

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')

    args = shlex.split(f'ping {shlex.quote(host)}')
    subprocess.run(args, check=True, shell=False)

    return {"status": "completed"}