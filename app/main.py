from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    safe_hosts = ['localhost', '127.0.0.1']
    return host in safe_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Untrusted host")
    result = subprocess.run(shlex.split(f'ping -c 4 {host}'), check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}