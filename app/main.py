from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host in ['127.0.0.1', '::1']:  # Allow only localhost for demonstration purposes
        subprocess.call(['ping', host])
    else:
        raise ValueError('Ping to non-localhost hosts is not allowed')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}