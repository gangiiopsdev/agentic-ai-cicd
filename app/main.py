from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.example.com']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Host not allowed')

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        command = shlex.split(f'ping {host}')
        subprocess.run(command, check=True)
    return {"status": "completed"}