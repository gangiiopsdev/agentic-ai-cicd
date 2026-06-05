from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_valid_host(host):
    # Regex check for valid IP address format
    return re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', host.strip())

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host input')
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, shell=False, check=True)
    return {"status": "completed"}