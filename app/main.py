from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.isnumeric() and len(host) < 4:
        return False
    cmd = ['ping', host]
    subprocess.run(cmd, check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {'status': 'invalid host'}
    return {'status': 'completed'}