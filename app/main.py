from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'another-example.com']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        args = shlex.split(f'ping {host}')
        subprocess.call(args)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}