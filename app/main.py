from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', quote(host)], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Failed to ping {host}: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)