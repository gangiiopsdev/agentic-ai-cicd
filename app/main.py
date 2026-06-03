from fastapi import FastAPI
import subprocess
from shlex import quote
generate_ping_command = lambda host: ['ping', quote(host)]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = ''.join(c for c in host if c.isalnum() or c in '.-:_')  # Sanitize input
    subprocess.call(generate_ping_command(safe_host))
    return {'status': 'completed'}