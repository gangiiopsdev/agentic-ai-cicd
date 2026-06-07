from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        args = ['ping', host]
        subprocess.call(args)
        return {'status': 'completed'}
    else:
        return {'error': 'Unauthorized host'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)