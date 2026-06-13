from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}