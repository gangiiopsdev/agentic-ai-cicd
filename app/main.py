from fastapi import FastAPI
import subprocess
import shlex
def execute_ping(host):
    try:
        # Use a whitelist for allowed hosts
        if host not in ['google.com', 'example.com']:
            raise ValueError('Host not allowed')
        result = subprocess.run(shlex.split(f'ping -c 1 {host}'), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return execute_ping(host)