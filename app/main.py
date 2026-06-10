from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Host is not allowed')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        subprocess.run(['ping', host], check=True, capture_output=True)
        return {"status": "completed", "output": subprocess.stdout.decode()}
    else:
        return {"status": "failed", "reason": "Host not allowed"}