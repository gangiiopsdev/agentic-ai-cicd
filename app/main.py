from fastapi import FastAPI
import subprocess
from shlex import quote

def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '._-')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    subprocess.run(['ping', '--'] + [quote(safe_host)], check=True, capture_output=True, text=True)
    return {'status': 'completed'}