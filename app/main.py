from fastapi import FastAPI
import subprocess
def validate_host(host: str) -> bool:
    # Add host validation logic here
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts
def ping(host: str) -> str:
    if not validate_host(host):
        raise ValueError('Invalid host')
    cmd = f'ping {host}'
    result = subprocess.run(cmd, shell=False, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout
    else:
        return 'Ping failed'
app = FastAPI()
@app.get("/ping")
def ping_handler(host: str):
    return ping(host)