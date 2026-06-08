from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    safe_hosts = ['example.com', 'test.com']  # List of allowed hosts
    return host in safe_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'error': 'Unauthorized host'}, 403
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)
    return {'status': 'completed'}