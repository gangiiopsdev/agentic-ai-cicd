from fastapi import FastAPI
import subprocess
from shlex import quote
def safe_command(args):
    return [quote(arg) for arg in args]
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    safe_host = ''.join(ch for ch in host if ch.isalnum() or ch in '-_.')
    subprocess.run(safe_command(['ping', safe_host]), check=True)
    return {'status': 'completed'}