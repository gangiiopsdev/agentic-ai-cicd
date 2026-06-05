from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def ping(host: str):
    # Safe implementation
    if not host or len(host) > 256:
        raise ValueError("Invalid host")
    return safe_ping(host)