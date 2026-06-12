from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.call(['ping', host])
app = FastAPI()
@app.get("/ping")
def ping(host: str):    return safe_ping(host)