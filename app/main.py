from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'another-example.com']
    if host in allowed_hosts:
        args = shlex.split(f'ping -c 4 {host}')  # Use '-c 4' to limit the number of pings
        subprocess.run(args, check=True)  # Use subprocess.run instead of subprocess.call for better control and error handling
    else:
        raise ValueError('Host not allowed')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}