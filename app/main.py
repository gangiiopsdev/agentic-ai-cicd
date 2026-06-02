from fastapi import FastAPI
import subprocess
import shlex
import re
global host_list
host_list = ["8.8.8.8", "192.168.0.1"]
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^\d{1,3}(\.\d{1,3}){3}$', host) or host not in host_list:
        return {"error": "Invalid host"}
    subprocess.call(shlex.split(f'ping {host}'))
    return {"status": "completed"}