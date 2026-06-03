from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def is_safe_hostname(hostname):
    pattern = r'^example\.com$|^test\.com$'
    return re.match(pattern, hostname) is not None

@app.get("/ping")
def ping(host: str):
    if not is_safe_hostname(host.replace(';', '')) or ';' in host:
        return {"status": "failed", "error": "Invalid host"}
    try:
        args = shlex.split(f'ping -c 4 {host}')
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}