from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host in ['localhost', '127.0.0.1']:  # Allow only trusted hosts for simplicity
        return subprocess.call(['ping', '-c', '4', host])
    else:
        raise ValueError('Untrusted host')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}