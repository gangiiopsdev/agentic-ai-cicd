from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Use a whitelist of allowed hosts
    if host in ['allowed_host1', 'allowed_host2']:
        subprocess.call(['ping', host])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}