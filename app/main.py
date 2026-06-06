from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> bool:
    allowed_hosts = ['example.com', 'another-example.com']
    if host in allowed_hosts:
        subprocess.call(['ping', host])
        return True
    else:
        return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}