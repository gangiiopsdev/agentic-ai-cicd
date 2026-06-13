from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_hostname(hostname):
    # Define a safe list of allowed hostnames or patterns
    safe_hosts = ['example.com', 'test.com']
    return any(hostname.endswith(safe_host) for safe_host in safe_hosts)

@app.get("/ping")
def ping(host: str):
    if not is_safe_hostname(host):
        raise HTTPException(status_code=403, detail="Invalid hostname")
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {"status": "completed"}