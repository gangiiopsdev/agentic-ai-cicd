from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'localhost']  # Example allowed hosts
    return host in allowed_hosts@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        try:
            args = ['ping', '-c', '1', host]  # Use specific arguments to avoid shell=True
            subprocess.run(args, check=True)
        except subprocess.CalledProcessError as e:
            raise ValueError('Ping failed') from e
    else:
        raise ValueError('Host not allowed')
    return {"status": "completed"}