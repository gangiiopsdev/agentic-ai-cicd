from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.strip():
        raise ValueError("Invalid host")
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'error': 'Host not allowed'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)