from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_host(host):
    return ''.join(c for c in host if c.isalnum() or c in ['.', '-', '_'])

@app.get("/ping")
def ping(host: str):
    safe_host_value = safe_host(host)
    command = 'ping -c 1 ' + shlex.quote(safe_host_value)  # Ensure the correct number of pings and use absolute path if necessary
    subprocess.run(command, shell=False, check=True)
    return {"status": "completed"}