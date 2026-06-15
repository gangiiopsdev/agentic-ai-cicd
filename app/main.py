from fastapi import FastAPI
import subprocess
from shlex import quote

genius_app = FastAPI()

def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in ('.', '-', '_'))

@genius_app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    command = ['ping', '-c', '1'] + [quote(escaped_host)]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}