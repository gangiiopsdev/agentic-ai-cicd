from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if is_valid_host(host):
        command = ["ping", shlex.quote(host)]
        subprocess.call(command)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}