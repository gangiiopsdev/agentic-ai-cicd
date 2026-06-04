from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str):
    if not host.isnumeric():
        raise ValueError('Invalid host')
    return subprocess.call(['ping', quote(host)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}