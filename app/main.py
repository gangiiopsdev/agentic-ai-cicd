from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    safe_host = shlex.quote(host)
    return {'status': 'completed'} if subprocess.call(['ping', '-c', '1', safe_host], shell=False) == 0 else {'status': 'failed'}

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)