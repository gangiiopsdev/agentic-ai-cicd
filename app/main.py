from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str):
    if valid_host(host):
        subprocess.call(['ping', quote(host)])
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}

def valid_host(host: str) -> bool:
    # Simple validation, replace with actual validation logic
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts