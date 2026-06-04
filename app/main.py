from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Sanitize input by checking allowed hosts or using a whitelist
    allowed_hosts = ['example.com', 'another-example.com']
    if host in allowed_hosts:
        subprocess.call(['ping', host])
    return {'status': 'completed'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)