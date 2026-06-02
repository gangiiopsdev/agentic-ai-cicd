from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def _validate_host(host):
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid hostname')

@app.get("/ping")
def ping(host: str):
    _validate_host(host)
    subprocess.call(['ping', shlex.quote(host)])
    return {"status": "completed"}