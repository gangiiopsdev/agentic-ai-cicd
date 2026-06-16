from fastapi import FastAPI
import subprocess
import shlex
def execute_ping(host):
    try:
        # Use a whitelist for allowed hosts
        allowed_hosts = ['google.com', 'example.com']
        if host not in allowed_hosts:
            raise ValueError('Host not allowed')
        result = subprocess.run(shlex.split(f'ping -c 1 {host}'), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return execute_ping(host)