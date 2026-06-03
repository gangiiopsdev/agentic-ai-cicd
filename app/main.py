from fastapi import FastAPI
import subprocess
import shlex
def is_valid_host(host):
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}