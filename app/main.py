from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if host.strip() == '' or not host.isalnum():
        return False
    try:
        subprocess.run(shlex.split('ping ' + host), check=True)
        return True
    except subprocess.CalledProcessError:
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed"}