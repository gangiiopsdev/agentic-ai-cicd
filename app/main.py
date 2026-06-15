from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    safe_host = host.replace(';', '').replace('&', '').replace('||', '')
    if not safe_host or 'ping' in safe_host:
        return {'error': 'Invalid input'}
    subprocess.call(['ping', safe_host])
    return {"status": "completed"}

@app.get("/ping")
def ping(host: str):
    return ping_safe(host)