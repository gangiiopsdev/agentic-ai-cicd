from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    # Implement a whitelist or other validation logic here
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    args = ['ping', shlex.quote(host)]
    subprocess.call(args)
    return {"status": "completed"}