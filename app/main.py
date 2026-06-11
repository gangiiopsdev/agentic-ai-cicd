from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Host not allowed')
    subprocess.call(['ping', subprocess.list2cmdline([host])])
    return {"status": "completed"}