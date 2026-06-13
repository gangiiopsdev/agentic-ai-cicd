from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if host.strip() == '' or not host.isalnum():
        return False
    try:
        # Use a whitelist for allowed hosts
        if host in ['example.com', 'test.com']:
            subprocess.run(shlex.split('ping ' + host), check=True)
            return True
    except subprocess.CalledProcessError:
        return False
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed"}