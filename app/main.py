from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host):
    try:
        subprocess.run(['ping', quote(host)], check=True, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'completed'}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return result