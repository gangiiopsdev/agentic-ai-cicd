from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    # Safe implementation using shell=False and args parameter
    if validate_host(host):
        result = await subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., check if the host is in a whitelist
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts