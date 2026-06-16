from fastapi import FastAPI
import subprocess
import shlex
def is_safe_host(host):
    # Implement a safe host check here
    return True if host in ['example.com', 'localhost'] else False
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Invalid host")
    command = shlex.split('ping -c 1 "{}"'.format(shlex.quote(host)))  # Limit the number of pings to mitigate DDoS risk
    subprocess.run(command, check=True)
    return {"status": "completed"}