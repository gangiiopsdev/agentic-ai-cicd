from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    allowed_hosts = ['127.0.0.1', 'localhost']  # Define allowed hosts
    if host in allowed_hosts:
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'status': 'denied'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)