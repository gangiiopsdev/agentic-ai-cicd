from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    safe_host = quote(host)
    subprocess.run(['ping', '-c', '1', safe_host], check=True, shell=False)
    return {'status': 'completed'}