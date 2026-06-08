from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'localhost']  # Example allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        subprocess.call(['ping'] + shlex.split(host))
    else:
        raise ValueError('Host not allowed')

    return {"status": "completed"}