from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def escape_host(host):
    return ''.join(char for char in host if char.isalnum() or char in ('.', '-'))

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    subprocess.call(['ping', quote(safe_host)], shell=False)
    return {"status": "completed"}