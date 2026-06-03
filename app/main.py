from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host and isinstance(host, str) and re.match(r'^[a-zA-Z0-9.-]+$', host): # basic validation for a hostname/IP
        args = ['ping', host]
        subprocess.run(args, check=True, shell=False)
    else:
        raise ValueError('Invalid host parameter')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}