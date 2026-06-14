from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str):
    if not host.isdigit():
        return False
    try:
        subprocess.call(['ping', '-c', '4', quote(host)], shell=False)
        return True
    except Exception as e:
        print(f'Error pinging {host}: {e}')
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed", "message": f'Successfully pinged {host}'}
    else:
        return {"status": "failed", "message": f'Failed to ping {host}'}