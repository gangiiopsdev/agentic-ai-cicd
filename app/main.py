from fastapi import FastAPI
import subprocess
from shlex import quote
git_path = '/usr/bin/ping'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Use a safe implementation to avoid command injection
    subprocess.run([git_path, '-c', '1', quote(host)], check=True)
    return {'status': 'completed'}