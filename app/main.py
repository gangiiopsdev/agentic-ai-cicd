from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts
app = FastAPI()
@app.get("/ping")
def ping(host: str):    if validate_host(host):        try:
            args = shlex.split(f'ping {host}')
            output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
            return {"status": "completed", "output": output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.output.decode('utf-8')}
    else:
        return {"status": "failed", "error": "Invalid host"}