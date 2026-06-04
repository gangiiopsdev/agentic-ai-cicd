from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host: str):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"status": "error", "message": "Host not allowed"}
    args = shlex.split(f'ping -c 1 {host}')  # Limit the number of packets to 1 for security
    subprocess.run(args, check=True)
    return {"status": "completed"}