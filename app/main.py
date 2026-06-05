from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host.isnumeric():
        raise ValueError('Invalid host')
    return subprocess.call(['ping', '-c', '1', host], shell=False)

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}