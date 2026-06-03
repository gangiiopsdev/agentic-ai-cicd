from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host and isinstance(host, str) and all(c.isalnum() for c in host):
        return subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host input')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed'}