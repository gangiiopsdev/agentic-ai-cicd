from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_hostname(hostname):
    # Implement safe hostname checking logic here
    return all(c.isalnum() or c in ['-', '_'] for c in hostname)

@app.get("/ping")
def ping(host: str):
    if is_safe_hostname(host):
        args = shlex.split(f'ping {host}')
        subprocess.call(args, shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid hostname"}