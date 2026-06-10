from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    safe_hosts = ['localhost', '127.0.0.1']
    return host in safe_hosts

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        subprocess.call(['/bin/ping', host])
        return {"status": "completed"}
    else:
        return {"status": "error", "message": "Invalid host"}