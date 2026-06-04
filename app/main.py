from fastapi import FastAPI
import subprocess
import shlex
import re
def is_safe_hostname(hostname):
    # Define a regular expression pattern for allowed hosts
    pattern = r'^example\.com$|^test\.com$'
    return re.match(pattern, hostname) is not None
app = FastAPI()
@app.get("/ping")
def ping(host: str):  
    if not is_safe_hostname(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        args = shlex.split(f'ping -c 4 {shlex.quote(host)}')
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}