from fastapi import FastAPI
import subprocess
import shlex
def is_safe_hostname(hostname):
    safe_hosts = ['example.com', 'test.com']
    return any(hostname.endswith(safe_host) for safe_host in safe_hosts)

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not is_safe_hostname(host):
        raise HTTPException(status_code=403, detail="Invalid hostname")
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}