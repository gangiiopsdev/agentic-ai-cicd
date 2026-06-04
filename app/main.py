from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    # Input validation to avoid code injection
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host not allowed'}
    safe_ping(host)
    return {'status': 'completed'}