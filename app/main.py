from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_hostname(hostname):
    # Implement safe hostname checking logic here
    return all(c.isalnum() or c in ['-', '_'] for c in hostname)

def safe_ping(host):
    if is_safe_hostname(host):
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    else:
        return "Invalid hostname"

@app.get("/ping")
def ping(host: str):
    try:
        return safe_ping(host)
    except subprocess.CalledProcessError as e:
        return str(e)