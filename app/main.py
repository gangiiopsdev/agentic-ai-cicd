from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host and host.isalnum():
        subprocess.call(['ping', host])
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    return {'status': safe_ping(host)}